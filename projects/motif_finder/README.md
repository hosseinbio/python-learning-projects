# DNA Motif Finder

A Python script designed to locate and analyze the positions and tandem repeats (repeated blocks) of a nucleotide motif within a given DNA sequence.

## Key Features

  * **Comprehensive Search:** Finds all occurrences of the motif, including **overlapping** positions.
  * **Tandem Repeat Analysis:** Identifies regions where the motif is repeated contiguously (e.g., `GCGCGC` for the motif `GC`).
  * **FASTA Input Support:** Handles multi-line sequences and ignores FASTA headers (`>...`).
  * **Structured Output:** Saves analysis results into multiple structured CSV files for easy post-analysis.

-----

## Installation and Setup

This script requires the `pandas` library. The `pathlib` module is used for modern path handling and is included in Python 3.

### 1\. Prerequisites

Ensure you have Python 3 installed on your system.

### 2\. Install Libraries

Install the required library using `pip`:

```bash
pip install pandas
```

-----

## How to Use

The script runs interactively, prompting the user for the sequence and the motif to search.

### 1\. Running the Script

Execute the script from your terminal:

```bash
python your_script_name.py
# (Replace with your script's filename)
```

### 2\. Inputs

The script will prompt you for two inputs:

1.  **DNA Sequence:**

      * You can enter a long, multi-line sequence or paste the content of a FASTA file (the script automatically removes the header).
      * The input is concluded by entering an empty line (pressing `Enter`).
      * **Example:**
        ```
        Enter your DNA sequence (multi-line FASTA allowed). Finish with an empty line:
        >sequence_id_1
        ATGCGTGCGTGCGTAT
        GCGTGCGT

        <Press Enter>
        ```

2.  **Motif to Search For:**

      * The motif must consist only of the characters A, T, G, C.
      * **Example:** `GCGT`

-----

## Output

The analysis results are saved in a sub-folder named **`output`** located in the same directory where the script is executed.

### Output Files

The script generates up to three CSV files (depending on whether occurrences or blocks were found):

| Filename | Content Description | Key Columns |
| :--- | :--- | :--- |
| `motif_results_summary.csv` | A high-level overview of the entire analysis. | `Motif`, `Sequence Length`, `Occurrences Count`, `Blocks Count` |
| `motif_results_positions.csv` | A list of every single position where the motif was found. | `Position (1-based)` |
| `motif_results_blocks.csv` | Detailed breakdown of the detected tandem repeat blocks. | `start`, `end`, `length`, `repeats` |

### Explanation of Blocks Columns

| Column | Description |
| :--- | :--- |
| `start` | The **1-based index** of the first character of the block. |
| `end` | The **0-based index** of the position *after* the last character of the block (useful for Python slicing). |
| `length` | The total length of the repetitive block in nucleotides. |
| `repeats` | The number of times the motif was completely repeated in the block. |

-----

## Example Execution

**Input:**

  * **Sequence:** `ATGCGCGCGCAT`
  * **Motif:** `GC`

**Console Output:**

```
=== RESULTS ===

Found 4 occurrences at positions (1-based): [3, 5, 7, 9]

Detected repeated motif blocks:
- Block at 3–11 (Repeats: 4, Length: 8)

Saving results...
Summary saved to: output/motif_results_summary.csv
Positions detail saved to: output/motif_results_positions.csv
Blocks detail saved to: output/motif_results_blocks.csv

Results saved successfully.
```

-----

> **Note:** The script accepts only A, T, G, C characters (case-insensitive) for sequences and motifs.
