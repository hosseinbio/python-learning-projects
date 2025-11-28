import os
import re
import pandas as pd


# ---------------------------
# Paths
# ---------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSV_PATH = os.path.join(OUTPUT_DIR, "Results.csv")


# ---------------------------
# Input Handling
# ---------------------------

def get_fasta_input():
    """
    Get a DNA sequence from the user in FASTA format.
    Returns the cleaned sequence or None if invalid.
    """

    print("Please insert your sequence in FASTA format:")
    print("(Finish by pressing Enter on an empty line)\n")

    lines = []
    while True:
        line = input().strip()
        if not line:
            break
        lines.append(line)

    if not lines:
        print("ERROR: No input received.")
        return None

    # Remove FASTA header if present
    if lines[0].startswith(">"):
        lines = lines[1:]

    seq = "".join(lines).upper()

    # Validate sequence
    valid_nt = {"A", "T", "C", "G"}
    if any(ch not in valid_nt for ch in seq):
        print("ERROR: Sequence contains invalid characters.")
        return None

    return seq


# ---------------------------
# Core Functions
# ---------------------------

def gc_content(seq):
    """Return GC percentage of a DNA sequence."""
    gc = sum(1 for nt in seq if nt in {"G", "C"})
    return (gc / len(seq)) * 100


def complement_nucleotide(nt):
    """Return complementary nucleotide."""
    mapping = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return mapping[nt]


def complement_sequence(seq):
    """Return complementary DNA sequence."""
    return "".join(complement_nucleotide(nt) for nt in seq)


def find_orf(seq):
    """
    Find the first ORF (start codon → multiple of 3 → stop codon).
    Returns the ORF string or None.
    """

    # Non-greedy, triplet-based ORF detection
    pattern = r"ATG(?:...)*?(?:TAA|TAG|TGA)"
    match = re.search(pattern, seq)

    return match.group() if match else None


# ---------------------------
# CSV Writing
# ---------------------------

def write_results_to_csv(seq, seq_len, gc, complementary, orf, orf_len):
    """Save analysis results to CSV."""

    df = pd.DataFrame({
        "Input sequence": [seq],
        "Sequence length": [seq_len],
        "GC content (%)": [gc],
        "Complementary sequence": [complementary],
        "ORF": [orf if orf else "None"],
        "ORF length": [orf_len],
    })

    df.to_csv(CSV_PATH, index=False)
    print(f"\nResults saved to: {CSV_PATH}\n")


# ---------------------------
# Main Pipeline
# ---------------------------

def analyze():
    seq = get_fasta_input()
    if seq is None:
        return

    seq_len = len(seq)
    gc = gc_content(seq)
    complementary = complement_sequence(seq)
    orf = find_orf(seq)
    orf_len = len(orf) if orf else 0

    write_results_to_csv(seq, seq_len, gc, complementary, orf, orf_len)

    print("Analysis complete.")
    print("---------------------")
    print(f"Length: {seq_len}")
    print(f"GC%: {gc:.2f}")
    print(f"Complementary: {complementary[:50]}{'...' if len(complementary)>50 else ''}")
    print(f"ORF: {orf if orf else 'No ORF found'}\n")


if __name__ == "__main__":
    analyze()
