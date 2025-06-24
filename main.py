# PROGETTO PSI - Analisi pubblicitaria (versione Python)
# Obiettivo: analizzare la relazione tra spesa pubblicitaria e fatturato

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

# Caricamento dati da file Excel
file_path = os.path.join(os.path.dirname(__file__), "dati.xlsx")
dati = pd.read_excel(file_path, sheet_name="dati")

# Analisi descrittiva
print(dati.describe())

# Calcolo della correlazione
correlazione = dati['Spesa_pubblicitaria'].corr(dati['Fatturato'])
print(f"Correlazione: {correlazione:.3f}")

# Regressione lineare
X = sm.add_constant(dati['Spesa_pubblicitaria'])
y = dati['Fatturato']
model = sm.OLS(y, X).fit()
print(model.summary())

# Calcolo delle predizioni e dei residui
dati['Fatturato_predetto'] = model.predict(X)
dati['Residui'] = dati['Fatturato'] - dati['Fatturato_predetto']

# Visualizzazione con subplots
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Primo grafico: dispersione + retta regressione
sns.regplot(
    x='Spesa_pubblicitaria',
    y='Fatturato',
    data=dati,
    ax=axes[0],
    line_kws={"color": "red"},
    scatter_kws={"color": "blue"}
)
axes[0].set_title("Spesa pubblicitaria vs Fatturato")
axes[0].set_xlabel("Spesa pubblicitaria (k€)")
axes[0].set_ylabel("Fatturato (k€)")

# Secondo grafico: residui
sns.residplot(
    x='Spesa_pubblicitaria',
    y='Residui',
    data=dati,
    ax=axes[1],
    lowess=True,
    color="green"
)
axes[1].set_title("Grafico dei residui")
axes[1].set_xlabel("Spesa pubblicitaria")
axes[1].set_ylabel("Residui")

plt.tight_layout()
plt.show()

# Il modello mostra una forte relazione positiva tra spesa pubblicitaria e fatturato.
# Il coefficiente angolare (~3.55) indica un aumento medio di 3.55k€ per ogni 1k€ speso.
# Il modello ha un R^2 di circa 0.62, quindi spiega una buona parte della variabilità.
# I residui sono ben distribuiti e non mostrano pattern anomali.