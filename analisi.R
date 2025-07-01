# PSI Progetto Luglio 2025
# Analisi Spesa pubblicitaria - Fatturato

# Librerie
library(ggplot2)
library(readxl)
library(car)

# Import dati
dati <- read_excel("C:\\Users\\simon\\Desktop\\Coding\\R\\dati.xlsx")

# Analisi descrittiva
summary(dati$Spesa_pubblicitaria)
summary(dati$Fatturato)
sd(dati$Spesa_pubblicitaria)
sd(dati$Fatturato)

# Istogrammi
ggplot(dati, aes(x=Spesa_pubblicitaria)) +
  geom_histogram(binwidth=100, fill="steelblue", color="black") +
  theme_minimal()

ggplot(dati, aes(x=Fatturato)) +
  geom_histogram(binwidth=1000, fill="tomato", color="black") +
  theme_minimal()

# Boxplot
ggplot(dati, aes(y=Spesa_pubblicitaria)) +
  geom_boxplot(fill="lightgreen") +
  theme_minimal()

ggplot(dati, aes(y=Fatturato)) +
  geom_boxplot(fill="lightblue") +
  theme_minimal()

# Scatterplot
ggplot(dati, aes(x=Spesa_pubblicitaria, y=Fatturato)) +
  geom_point() +
  geom_smooth(method="lm", se=TRUE, color="red") +
  theme_minimal()

# Correlazione
cor(dati$Spesa_pubblicitaria, dati$Fatturato)

# Regressione
modello <- lm(Fatturato ~ Spesa_pubblicitaria, data=dati)
summary(modello)

# Diagnostica residui
plot(modello, which=1) # Residui vs valori stimati
plot(modello, which=2) # QQ-plot
shapiro.test(residuals(modello)) # test normalità residui

# Cook's distance
influencePlot(modello)