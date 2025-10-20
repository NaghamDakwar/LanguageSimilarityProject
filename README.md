# Language Similarity Between Couples - Data Analysis

This project analyzes language similarity among heterosexual couples by computing three similarity metrics in text and examining correlation with relationship measures. 
This analysis is conducted by Python code and R code.

## Objective

**Python script** - To convert transcripts in .docx format into a file in .csv format.

**R script** - To measure the degree of similarity in language use between partners in heterosexual couples (male and female), and explore how this relates to self-reported measures in their relationships (i.e., Closeness, RAS, IRIC-PT, IRIC-EC).

## Input Format 

**Python script**: The input file is a .docx format. 
- Each subject's transcript starts with a new line. 
- Each subject is represented by identifier, dyad and gender, underlined and bold (e.g., **<u>123456789_12_F</u>**)
- Each answer is represented by identifier, dyad and question number, underlined (e.g., <u>123456789_12_5</u>)
- Each answer starts with a new line under answer identifier.

**R script**: The input file must be a CSV with the following columns:

- `subject`: Unique identifier for each participant.
- `dyad`: A shared ID (dyad) for both partners in a couple.
- `gender`: Identifier for participant's gender (e.g., "male", "female").
- `Q1` to `Q6`: 6 columns, each column contains the participant's answer. The answer format is an array of strings (e.g., ['היה', 'קטע', 'מצחיק']).

## Measures

The project computes the following indices for each couple:

- **Cosine Similarity**: A metric that quantifies the similarity between two word vectors in muilti-dimensional space.
- **TTR (Type-Token Ratio) Difference**: Measures the lexical diversity in a text, calculated by dividung the number of unique words (types) by the total number of words (tokens). The difference between partners is then calculated.
- **Word Uniqueness Difference**: For each participant, the average uniqueness of used words is computed based on a frequency corpus built from the experiment. The difference between partners is then calculated.

The similarity indices are calculated:

-For each individual answer (there are 6 responses per participant).
-And again for the entire concatenated text (all 6 answers combined).

Each of these indices is compared to **Null Distribution**, built by generating 10,000 samples of random fake couples to evaluate significance.

Additionally, for each similarity index, **Pearosn correlation** is computed with **4 questionnaire scores** and measuring relationship satisfaction.

## File Overview

- `TranscriptsProcessing.py` – Python file that coverts transcripts in .docx format into a file in .csv format. Each row represents a subject, with their transcripts converted into array of strings. 
- `TextSimilarity.Rmd` – Main R Markdown file performing the analysis and generating results.
- `README.md` – This documentation file.

## Requirements

This project was developed and tested using:

- **Python version 3.12.0**, compatible with Python ≥ 3.8.
- **R version 4.5.0**, compatible with R ≥ 4.0.0.

- The required **Python packages** are:

```r
pip install pandas python-docx
```

- The required **R packages** are:

```r
install.packages(c(
  "tidyverse", "tm", "stringr", "proxy", "readr",
  "tibble", "dplyr", "purrr", "ggplot2", "psych"
))
```

## Workflow 

Python (data preprocessing) → CSV output → R (statistical analysis)
