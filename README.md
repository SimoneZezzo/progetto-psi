# PSI Project – Analysis of the Relationship Between Advertising Expenses and Revenue

This project performs a statistical analysis to study the relationship between advertising expenses and company revenue. It was initially developed in R for the university exam “Probability and Statistics for Computer Science,” and later replicated in Python as an alternative implementation.

---

## Project Structure

- **`analisi.R`**  
  R script performing:
  - descriptive analysis
  - scatter plots
  - linear regression
  - summary statistics
  - residual analysis

- **`main.py`**  
  Python script implementing the same analysis, including:
  - descriptive analysis
  - scatter plots and residual plots
  - linear regression
  - integrated comments explaining the output

- **`dati.xlsx`**  
  Excel file containing the dataset provided by the instructor.

- **`Analisi Spesa Pubblicitaria e Fatturato-Final.pdf`**  
  Final report summarizing the results of the analysis, including charts and interpretation of the statistical findings.

- **`README.md`**  
  This file.

---

## Requirements

### R Environment

- R version ≥ 4.0 recommended
- Required R packages:
  - `readxl`
  - `ggplot2`

Install the necessary packages in R:

```R
install.packages("readxl")
install.packages("ggplot2")
```

### Python Environment

- Python 3.11 recommended  
  (avoid Python 3.13 due to compatibility issues with `statsmodels`)
- Virtual environment activated
- Required Python packages:

```bash
pip install pandas seaborn matplotlib statsmodels openpyxl
```

---

## How to Run the Analysis

### Running the R Script

1. Open R or RStudio.
2. Set the working directory to the project folder:
   ```R
   setwd("path/to/progetto-psi")
   ```
3. Run the script:
   ```R
   source("analisi.R")
   ```

The script will read the Excel data and generate plots and regression results.

---

### Running the Python Script

1. Navigate to the project folder:
   ```bash
   cd path/to/progetto-psi
   ```

2. Activate the virtual environment:
   ```bash
   path\to\env\Scripts\activate      # Windows
   # or
   source path/to/env/bin/activate   # macOS/Linux
   ```

3. Run the Python script:
   ```bash
   python main.py
   ```

---

## Final Report

The file **Analisi Spesa Pubblicitaria e Fatturato-Final.pdf** contains:

- All the plots created during the analysis
- Interpretation of the statistical results
- Conclusions drawn from the relationship between advertising expenses and revenue

---

## Author

Developed as part of the coursework for the Probability and Statistics for Computer Science exam.