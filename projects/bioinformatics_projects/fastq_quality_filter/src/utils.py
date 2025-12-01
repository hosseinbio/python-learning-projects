"""
utils.py
Utility functions for FASTQ quality processing.

Place in:
projects/bioinformatics_projects/fastq_quality_filter/src/utils.py
"""

import gzip
from typing import Iterator, Tuple, List, TextIO
import statistics
import os


def open_maybe_gzip(path: str, mode: str = "rt") -> TextIO:
    """
    Open text file, support .gz transparently.
    mode default 'rt' (read text). Use 'wt' for writing.
    """
    if path.endswith(".gz"):
        return gzip.open(path, mode)
    return open(path, mode, encoding="utf-8")


def read_fastq(path: str) -> Iterator[Tuple[str, str, str, str]]:
    """
    Generator to read FASTQ records from `path`.
    Yields (header, seq, plus, qual) for each record.

    Raises ValueError on incomplete final record.
    """
    with open_maybe_gzip(path, "rt") as fh:
        lines = []
        for line in fh:
            lines.append(line.rstrip("\n\r"))
            if len(lines) == 4:
                header, seq, plus, qual = lines
                # Basic validation
                if not header.startswith("@"):
                    raise ValueError(f"FASTQ header does not start with '@': {header!r}")
                if not plus.startswith("+"):
                    raise ValueError(f"FASTQ plus line does not start with '+': {plus!r}")
                yield header, seq, plus, qual
                lines = []
        if lines:
            raise ValueError(f"Incomplete FASTQ record in file {path}")


def phred33_to_q(ch: str) -> int:
    """Convert a single Phred+33 character to integer quality."""
    if len(ch) != 1:
        raise ValueError("phred33_to_q expects a single character")
    return ord(ch) - 33


def phred33_to_qs(qual: str) -> List[int]:
    """Convert quality string to list of Phred scores."""
    return [phred33_to_q(c) for c in qual]


def read_quality_stats(qual: str, min_q: int) -> Tuple[int, int, float, float]:
    """
    Given a quality string and threshold min_q, returns:
      (total_bases, num_pass, percent_pass (0..100), mean_q)
    """
    qs = phred33_to_qs(qual)
    total = len(qs)
    if total == 0:
        return 0, 0, 0.0, 0.0
    num_pass = sum(1 for q in qs if q >= min_q)
    percent = (num_pass / total) * 100
    mean_q = statistics.mean(qs)
    return total, num_pass, percent, mean_q


def write_fastq_record(fh: TextIO, record: Tuple[str, str, str, str]) -> None:
    """Write a FASTQ record (header, seq, plus, qual) to filehandle."""
    header, seq, plus, qual = record
    fh.write(f"{header}\n{seq}\n{plus}\n{qual}\n")


class StatsCollector:
    """
    Collect high-level per-run statistics.
    - total_reads
    - accepted_reads
    - rejected_reads
    - mean_q_before / mean_q_after
    """

    def __init__(self):
        self.total_reads = 0
        self.accepted_reads = 0
        self.rejected_reads = 0
        self.mean_qs_before = []
        self.mean_qs_after = []

    def add_read(self, qual: str, accepted: bool):
        self.total_reads += 1
        # compute mean q for the read
        _, _, _, mean_q = read_quality_stats(qual, min_q=0)
        self.mean_qs_before.append(mean_q)
        if accepted:
            self.accepted_reads += 1
            self.mean_qs_after.append(mean_q)
        else:
            self.rejected_reads += 1

    def summary(self) -> dict:
        avg_before = statistics.mean(self.mean_qs_before) if self.mean_qs_before else 0.0
        avg_after = statistics.mean(self.mean_qs_after) if self.mean_qs_after else 0.0
        accepted_fraction = (self.accepted_reads / self.total_reads * 100) if self.total_reads else 0.0
        return {
            "total_reads": self.total_reads,
            "accepted_reads": self.accepted_reads,
            "rejected_reads": self.rejected_reads,
            "mean_q_before": round(avg_before, 2),
            "mean_q_after": round(avg_after, 2),
            "accepted_fraction_percent": round(accepted_fraction, 2)
        }
