"""
pytest tests for utils.py

Run from the project-root or within the tool folder:
$ pytest projects/bioinformatics_projects/fastq_quality_filter/tests -q
"""

import sys
import os
import io
import tempfile

# ensure src directory is in path
THIS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import utils


def test_phred_conversion():
    # Q = 30 -> chr(33+30) = '?'
    q_char = chr(33 + 30)
    assert utils.phred33_to_q(q_char) == 30
    assert utils.phred33_to_qs(q_char * 5) == [30, 30, 30, 30, 30]


def test_read_quality_stats():
    # create quality string: 5 bases Q=30, 5 bases Q=10
    qual = chr(33 + 30) * 5 + chr(33 + 10) * 5
    total, num_pass, percent, mean_q = utils.read_quality_stats(qual, min_q=20)
    assert total == 10
    assert num_pass == 5
    assert percent == 50.0
    assert mean_q == (30 * 5 + 10 * 5) / 10


def test_read_fastq_and_stats(tmp_path):
    content = (
        "@r1\n"
        "ATGC\n"
        "+\n"
        f"{chr(33+30)}{chr(33+30)}{chr(33+30)}{chr(33+30)}\n"
        "@r2\n"
        "TTAA\n"
        "+\n"
        f"{chr(33+10)}{chr(33+10)}{chr(33+10)}{chr(33+10)}\n"
    )
    p = tmp_path / "sample.fastq"
    p.write_text(content, encoding="utf-8")

    records = list(utils.read_fastq(str(p)))
    assert len(records) == 2
    assert records[0][0].startswith("@r1")
    # stats on first read
    total, num_pass, percent, mean_q = utils.read_quality_stats(records[0][3], min_q=20)
    assert total == 4
    assert num_pass == 4
    assert percent == 100.0
