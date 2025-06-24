# Progetto PSI – Analisi della relazione tra spesa pubblicitaria e fatturato

Questo progetto esegue un'analisi statistica con grafici annessi secondo le linee guida di un progetto per l'esame Probabilità e Statistica per l'Informatica. Il progetto iniziale è stato richiesto in R, dopo averlo svolto ho esplorato Python come seconda opzione.

---

## Contenuto del progetto

- `main.py`: script Python contenente l’intera analisi, inclusi:
  - analisi descrittiva
  - grafici a dispersione e residui
  - regressione lineare
  - commenti integrati
- `dati.xlsx`: file Excel con i dati forniti dal docente
- `README.md`: questo file

---

## Requisiti

- **Python 3.11** consigliato (evitare Python 3.13 per incompatibilità con `statsmodels`)
- Ambiente virtuale attivo
- Pacchetti Python richiesti:

```bash
pip install pandas seaborn matplotlib statsmodels openpyxl
```

## Esecuzione

### Metodo consigliato (ambiente virtuale `psi-env`)

1. Entra nella cartella del progetto:
   ```
   cd nome_cartella_progetto
   ```

2. Attiva l’ambiente virtuale:
   ```bash
   path\to\env\Scripts\activate
   ```

3. Avvia lo script:
   ```bash
   python main.py
   ```
