"""
main.py
CLI wrapper for FASTQ quality filtering.

Place in:
projects/bioinformatics_projects/fastq_quality_filter/src/main.py
"""

import argparse
import os
from typing import Optional

from utils import (
    read_fastq,
    read_quality_stats,
    write_fastq_record,
    StatsCollector,
    open_maybe_gzip
)


def filter_record(qual: str, min_q: int, min_percent: float) -> bool:
    """
    Decide whether a single read (quality string) passes.
    Returns True if percent of bases with Q >= min_q is >= min_percent.
    """
    _, _, percent, _ = read_quality_stats(qual, min_q)
    return percent >= min_percent


def run_filter(input_path: str, output_path: str,
               min_q: int, min_percent: float,
               stats_path: Optional[str] = None) -> dict:
    """
    Run filtering over input_path FASTQ and write filtered reads to output_path.
    Returns summary dict.
    """
    stats = StatsCollector()

    # ensure output directory exists
    out_dir = os.path.dirname(output_path) or "."
    os.makedirs(out_dir, exist_ok=True)

    with open_maybe_gzip(output_path, "wt") as out_fh:
        for header, seq, plus, qual in read_fastq(input_path):
            accepted = filter_record(qual, min_q, min_percent)
            stats.add_read(qual, accepted)
            if accepted:
                write_fastq_record(out_fh, (header, seq, plus, qual))

    # optional stats report
    if stats_path:
        os.makedirs(os.path.dirname(stats_path) or ".", exist_ok=True)
        with open(stats_path, "w", encoding="utf-8") as fh:
            fh.write("FASTQ Quality Filter Report\n")
            fh.write("===========================\n")
            fh.write(f"Input: {input_path}\n")
            fh.write(f"Output: {output_path}\n")
            fh.write(f"Min Q: {min_q}\n")
            fh.write(f"Min Percent: {min_percent}\n\n")
            for k, v in stats.summary().items():
                fh.write(f"{k}: {v}\n")

    return stats.summary()


def build_argparser():
    parser = argparse.ArgumentParser(
        description="Filter FASTQ reads by base quality (Phred+33)."
    )
    parser.add_argument("--input", "-i", required=True, help="Input FASTQ file (.fastq or .fastq.gz)")
    parser.add_argument("--output", "-o", required=True, help="Filtered FASTQ output path (.fastq or .gz)")
    parser.add_argument("--min-quality", "-q", type=int, default=20, help="Minimum base quality (default 20)")
    parser.add_argument("--min-percent", "-p", type=float, default=80.0, help="Minimum percent bases >= min-quality (default 80.0)")
    parser.add_argument("--stats", "-s", default=None, help="Optional path to write summary statistics report")
    return parser


def main():
    parser = build_argparser()
    args = parser.parse_args()
    summary = run_filter(
        input_path=args.input,
        output_path=args.output,
        min_q=args.min_quality,
        min_percent=args.min_percent,
        stats_path=args.stats
    )

    print("\nFiltering done. Summary:")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
