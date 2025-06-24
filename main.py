# PROGETTO PSI - Analisi pubblicitaria (versione Python)
# Obiettivo: analizzare la relazione tra spesa pubblicitaria e fatturato

# 1. Importazione pacchetti
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 2. Caricamento dati da file Excel
import os
file_path = os.path.join(os.path.dirname(__file__), "dati.xlsx")
dati = pd.read_excel(file_path, sheet_name="dati")

# 3. Analisi descrittiva
print(dati.describe())

# Calcolo della correlazione
correlazione = dati['Spesa_pubblicitaria'].corr(dati['Fatturato'])
print(f"Correlazione: {correlazione:.3f}")

# 4. Grafico di dispersione con retta di regressione
sns.set(style="whitegrid")
plt.figure()
sns.regplot(x='Spesa_pubblicitaria', y='Fatturato', data=dati, ci=None, color='blue', line_kws={'color': 'red'})
plt.title("Spesa pubblicitaria vs Fatturato")
plt.xlabel("Spesa pubblicitaria (in migliaia di euro)")
plt.ylabel("Fatturato (in migliaia di euro)")
plt.tight_layout()
plt.show()

# 5. Regressione lineare
X = sm.add_constant(dati['Spesa_pubblicitaria'])
y = dati['Fatturato']
model = sm.OLS(y, X).fit()
print(model.summary())

# 6. Calcolo delle predizioni e dei residui
dati['Fatturato_predetto'] = model.predict(X)
dati['Residui'] = dati['Fatturato'] - dati['Fatturato_predetto']

# 7. Grafico dei residui
plt.figure()
sns.residplot(x='Spesa_pubblicitaria', y='Residui', data=dati, lowess=True, color='green')
plt.title("Grafico dei residui")
plt.xlabel("Spesa pubblicitaria")
plt.ylabel("Residui")
plt.tight_layout()
plt.show()

# 8. Conclusione (commentata nel codice)
# Il modello mostra una forte relazione positiva tra spesa pubblicitaria e fatturato.
# Il coefficiente angolare (~3.55) indica un aumento medio di 3.55k€ per ogni 1k€ speso.
# Il modello ha un R^2 di circa 0.62, quindi spiega una buona parte della variabilità.
# I residui sono ben distribuiti e non mostrano pattern anomali.

# Fine script