# FASTQ Quality Filter

A lightweight and practical command-line tool for filtering FASTQ reads
based on **minimum base quality** and **minimum percentage of high-quality bases**.

This tool is designed for molecular biology and bioinformatics students
who want to build real data-processing pipelines without relying on heavy external dependencies.

---

## Features

- Filters FASTQ reads by:
  - `--min-quality` → minimum accepted Phred score  
  - `--min-percent` → minimum percentage of bases meeting the quality threshold
- Supports both **single-end FASTQ** and **gzipped FASTQ** (coming soon)
- Validates FASTQ structure automatically
- Outputs a clean FASTQ file with only the reads that pass the quality filter
- Fully tested with **pytest**

---

## How to Run

### **1. Navigate to the project**

```bash
cd fastq_quality_filter/src
```

### **2. Run the script**

python main.py \
    --input ../input/sample.fastq \
    --output ../output/filtered.fastq \
    --min-quality 30 \
    --min-percent 80 \
    --stats

---

## Output Example

```
Processing: 12000 reads
Passed:     8750 reads
Failed:     3250 reads

Saved filtered reads → ../output/filtered.fastq
```

---

## Running Tests

Inside the project root:

```bash
pytest
```

You should see:

```
3 passed
```

---

## Why This Project Matters

This project demonstrates your ability to:

* Work with a real biological file format (FASTQ)
* Handle input parsing, validation, and error-proof logic
* Build a clean and modular codebase (`utils`, CLI, tests)
* Implement bioinformatics-style command-line tools
* Follow production-level folder structure & testing

This is a **great CV project** for roles like:

* Bioinformatics Intern
* Computational Biology Research Assistant
* Python Data Processing Developer
* Graduate-level genomics pipeline assistant

---

## Contact

Author: **Hossein Gholami**
LinkedIn: *[https://linkedin.com/in/hossein-gholami-9a6016301](https://linkedin.com/in/hossein-gholami-9a6016301)*
