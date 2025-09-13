# ==============================
# Análisis de tráfico en Dublín
# Objetivo: Encontrar el día con más tráfico en el año 2021
# ==============================

# 1. Importar librerías
import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
# Asegúrate de tener el archivo "traffic_flow.csv" en la misma carpeta que este script
df = pd.read_csv("traffic_flow.csv")

# 3. Convertir la columna DateTime a tipo fecha-hora (formato día/mes/año)
df["DateTime"] = pd.to_datetime(df["DateTime"], dayfirst=True)


# 4. Calcular el tráfico total cada 5 minutos
# Sumamos todos los sensores (columnas 0 hasta 32)
df["Total_5min"] = df.iloc[:, 1:].sum(axis=1)

# 5. Crear una columna solo con la fecha (sin hora)
df["Fecha"] = df["DateTime"].dt.date

# 6. Calcular el tráfico total diario
trafico_diario = df.groupby("Fecha")["Total_5min"].sum()

# 7. Encontrar el día con más tráfico
dia_max = trafico_diario.idxmax()   # Fecha con mayor tráfico
valor_max = trafico_diario.max()    # Número de vehículos ese día

print("El día con más tráfico fue:", dia_max, "con", valor_max, "vehículos")

# 8. Graficar el tráfico diario durante todo el año
plt.figure(figsize=(12,5))
trafico_diario.plot()
plt.title("Tráfico total por día en 2021 (Dublín)")
plt.xlabel("Fecha")
plt.ylabel("Número de vehículos")
plt.show()

print("📌 El día con más tráfico fue:", dia_max, "con", valor_max, "vehículos en total")

