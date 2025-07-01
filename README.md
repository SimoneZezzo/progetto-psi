# Progetto PSI – Analisi della relazione tra spesa pubblicitaria e fatturato

Progetto in Python e R per l’esame di Probabilità e Statistica per l’Informatica all’Università di Milano-Bicocca, Corso di Laurea in Informatica, con annessa analisi dei dati.

---

## Struttura del progetto

- **`analisi.R`**  
  Script R che esegue:
  - analisi descrittiva
  - grafici a dispersione
  - regressione lineare
  - statistiche riassuntive
  - analisi dei residui

- **`main.py`**  
  Script Python che implementa la stessa analisi, inclusi:
  - analisi descrittiva
  - grafici a dispersione e dei residui
  - regressione lineare
  - commenti integrati per spiegare i risultati

- **`dati.xlsx`**  
  File Excel contenente il dataset fornito dal docente.

- **`Analisi Spesa Pubblicitaria e Fatturato-Final.pdf`**  
  Relazione finale che riassume i risultati dell’analisi, inclusi grafici e interpretazione dei risultati statistici.

- **`README.md`**  
  Questo file.

---

## Requisiti

### Ambiente R

- Versione R ≥ 4.0 consigliata
- Pacchetti R richiesti:
  - `readxl`
  - `ggplot2`

Installa i pacchetti necessari in R:

```R
install.packages("readxl")
install.packages("ggplot2")
```

### Ambiente Python

- Python 3.11 consigliato  
  (evitare Python 3.13 per incompatibilità con `statsmodels`)
- Ambiente virtuale attivo
- Pacchetti Python richiesti:

```bash
pip install pandas seaborn matplotlib statsmodels openpyxl
```

---

## Come eseguire l’analisi

### Esecuzione dello script R

1. Apri R o RStudio.
2. Imposta la cartella di lavoro sulla cartella del progetto:
   ```R
   setwd("percorso/alla/cartella/progetto-psi")
   ```
3. Esegui lo script:
   ```R
   source("analisi.R")
   ```

Lo script leggerà i dati dal file Excel e genererà grafici e risultati della regressione.

---

### Esecuzione dello script Python

1. Spostati nella cartella del progetto:
   ```bash
   cd percorso/alla/cartella/progetto-psi
   ```

2. Attiva l’ambiente virtuale:
   ```bash
   path\to\env\Scripts\activate      # Windows
   # oppure
   source path/to/env/bin/activate   # macOS/Linux
   ```

3. Esegui lo script Python:
   ```bash
   python main.py
   ```

---

## Relazione finale

Il file **Analisi Spesa Pubblicitaria e Fatturato-Final.pdf** contiene:

- tutti i grafici creati durante l’analisi
- interpretazione dei risultati statistici
- conclusioni sulla relazione tra spesa pubblicitaria e fatturato

---

## Autore

Sviluppato nell’ambito dell’esame di Probabilità e Statistica per l’Informatica presso l’Università di Milano-Bicocca.