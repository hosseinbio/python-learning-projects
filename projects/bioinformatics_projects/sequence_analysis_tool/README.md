# DNA Sequence Analyzer

This Python script is designed to take a DNA sequence input in **FASTA format** and perform basic bioinformatics analyses, such as calculating the GC percentage, finding the complementary sequence, and detecting the first Open Reading Frame (ORF). The analysis results are then saved to a CSV file.

-----

## Features

  * **FASTA Input Handling:** Reads the DNA sequence from user input, supporting the optional FASTA header (the line starting with `>`).
  * **Sequence Validation:** Ensures the input sequence only contains valid DNA nucleotides (**A, T, C, G**).
  * **GC Content Calculation:** Computes the percentage of Guanine (G) and Cytosine (C) bases in the sequence.
  * **Complementary Sequence:** Generates the complementary DNA strand (A $\rightarrow$ T, C $\rightarrow$ G, etc.).
  * **ORF Detection:** Locates the first **Open Reading Frame** in the sequence (starting with `ATG` and ending with `TAA`, `TAG`, or `TGA`).
  * **CSV Reporting:** Saves all analysis results into a structured CSV file.

-----

## Requirements

The script requires the following Python libraries:

  * **`os`** (Standard Library)
  * **`re`** (Standard Library)
  * **`pandas`**

You can install `pandas` using `pip`:

```bash
pip install pandas
```

-----

## How to Run

1.  **Execute the Script:**

    ```bash
    python your_script_name.py
    ```

2.  **Provide Input:**
    When prompted, paste or type your DNA sequence in **FASTA format**. You can include the FASTA header or just the sequence. **Press Enter on an empty line** to finish the input.

    **Input Example:**

    ```
    Please insert your sequence in FASTA format:
    (Finish by pressing Enter on an empty line)

    >Sample_Gene_X
    ATGGACCGGATTTAAGGGTGTGA
    [Press Enter on an empty line]
    ```

3.  **View Results:**

      * A summary of the analysis will be printed to the console.
      * A detailed CSV file named **`Results.csv`** will be saved inside the automatically created `../output/` directory.

-----

## Project Structure

```
.
├── your_script_name.py  # (The main script file)
└── output
    └── Results.csv      # (The generated output file)
```

-----

## Technical Details

  * **Output Path:** Results are saved to the `../output/` directory, which is created if it does not already exist. The full path is derived relative to the script's location.
  * **ORF Detection:** The script uses a non-greedy regular expression for finding the first complete ORF:
    $$r"ATG(?:...)*?(?:TAA|TAG|TGA)"$$
    This pattern looks for the nearest combination of a **Start Codon** (`ATG`) followed by a multiple of three nucleotides (`(?:...)*?`) and ending in a **Stop Codon** (`TAA|TAG|TGA`).
    