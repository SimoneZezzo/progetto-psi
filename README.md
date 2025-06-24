# 📈 Progetto PSI – Analisi della relazione tra spesa pubblicitaria e fatturato

Questo progetto esegue un'analisi statistica utilizzando Python per studiare la relazione tra la spesa pubblicitaria e il fatturato settimanale di un'azienda, secondo le linee guida dell'esercitazione PSI (Università degli Studi di Milano-Bicocca).

---

## 📁 Contenuto del progetto

- `r.py`: script Python contenente l’intera analisi, inclusi:
  - analisi descrittiva
  - grafici a dispersione e residui
  - regressione lineare
  - commenti integrati
- `dati(1).xlsx`: file Excel con i dati forniti dal docente
- `grafico1.png` *(opzionale)*: grafico della relazione tra spesa pubblicitaria e fatturato
- `residui.png` *(opzionale)*: grafico dei residui della regressione
- `README.md`: questo file

---

## 📦 Requisiti

Assicurati di avere Python ≥ 3.10 e i seguenti pacchetti installati nel tuo ambiente:

```bash
pip install pandas seaborn matplotlib statsmodels openpyxl
```

⚠️ **Importante**: **non usare Python 3.13**, causa problemi di compatibilità con `statsmodels`.

---

## ⚙️ Esecuzione

### ▶ Metodo consigliato (ambiente virtuale `psi-env`)

1. Entra nella cartella del progetto:
   ```bash
   cd "C:\Users\simon\Desktop\Coding\Python\stat\fatturato_pubblicità"
   ```

2. Attiva l’ambiente virtuale:
   ```bash
   ..\..\course\psi-env\Scripts\activate
   ```

3. Avvia lo script:
   ```bash
   python r.py
   ```

---

## 📊 Cosa fa lo script

- Carica il file Excel con i dati
- Calcola statistiche descrittive per spesa pubblicitaria e fatturato
- Calcola la correlazione lineare
- Crea un **grafico a dispersione** con retta di regressione
- Esegue una **regressione lineare**
- Calcola e visualizza i **residui del modello**
- Commenta i risultati direttamente nel codice

---

## 📝 Obiettivo accademico

Il progetto è pensato per ottenere **2/2** nella valutazione, soddisfacendo i seguenti criteri:

- ✔️ Analisi descrittiva ben strutturata
- ✔️ Uso di grafici chiari e commentati
- ✔️ Regressione ben eseguita e interpretata
- ✔️ Codice pulito e narrato
- ✔️ Nessun errore tecnico

---

## 👨‍🎓 Autore

**Simone Z.**  
Corso di Laurea in Informatica – a.a. 2024/2025  
Università degli Studi di Milano-Bicocca
