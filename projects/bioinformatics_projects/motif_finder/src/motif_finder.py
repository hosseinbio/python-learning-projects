import os
import pandas as pd


# ============= CORE LOGIC ============= #

def find_motif_positions(seq: str, motif: str):
    """
    Finds ALL occurrences (overlapping + non-overlapping).
    Returns 1-based positions.
    """
    positions = []
    m = len(motif)

    for i in range(len(seq) - m + 1):
        if seq[i:i + m] == motif:
            positions.append(i + 1)

    return positions


def find_motif_blocks(seq: str, motif: str):
    """
    Finds repeated blocks of motif (e.g. GC repeated 4x).
    Returns list of dicts: {start, end, length, repeats}
    """
    blocks = []
    i = 0
    m = len(motif)

    while i < len(seq):
        if seq[i:i + m] == motif:
            start = i

            while seq[i:i + m] == motif:
                i += m

            end = i  # 1-based friendly
            block_len = end - start
            repeats = block_len // m

            blocks.append({
                "start": start + 1,
                "end": end,
                "length": block_len,
                "repeats": repeats
            })
        else:
            i += 1

    return blocks


def generate_csv(seq, motif, positions, blocks, output_path):
    """
    Save analysis into CSV.
    """
    df = pd.DataFrame({
        "Motif": [motif],
        "Sequence Length": [len(seq)],
        "Occurrences Count": [len(positions)],
        "Occurrences Positions (1-based)": [positions],
        "Blocks Count": [len(blocks)],
        "Blocks Detail": [blocks]
    })

    df.to_csv(output_path, index=False)


# ============= INPUT HANDLING ============= #

def get_user_input_sequence():
    print("Enter your DNA sequence (multi-line FASTA allowed). Finish with empty line:")

    lines = []
    while True:
        line = input().strip()
        if line == "":
            break
        lines.append(line)

    # remove FASTA header
    if lines and lines[0].startswith(">"):
        lines.pop(0)

    seq = "".join(lines).upper()

    # validate
    if not all(c in "ATGC" for c in seq):
        raise ValueError("Sequence contains invalid characters. Only A/T/G/C allowed.")

    return seq


def get_user_input_motif():
    motif = input("Enter the motif to search for: ").strip().upper()

    if not motif or not all(c in "ATGC" for c in motif):
        raise ValueError("Motif must only contain A/T/G/C.")

    return motif


# ============= MAIN FUNCTION ============= #

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "output"))
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "motif_results.csv")

    print("\n--- MOTIF FINDER ---\n")

    try:
        seq = get_user_input_sequence()
        motif = get_user_input_motif()
    except ValueError as e:
        print(f"Input Error: {e}")
        return

    positions = find_motif_positions(seq, motif)
    blocks = find_motif_blocks(seq, motif)

    # show results
    print("\n=== RESULTS ===\n")

    if positions:
        print(f"Found {len(positions)} occurrences at positions: {positions}")
    else:
        print("No individual motif occurrences found.")

    print()

    if blocks:
        print("Detected repeated motif blocks:")
        for b in blocks:
            print(f"- Block at {b['start']}–{b['end']} (repeats: {b['repeats']})")
    else:
        print("No repeated motif blocks found.")

    # save CSV
    generate_csv(seq, motif, positions, blocks, output_path)

    print(f"\nResults saved to:\n{output_path}")


if __name__ == "__main__":
    main()
