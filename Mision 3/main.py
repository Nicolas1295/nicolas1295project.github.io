# ============================================================
# archivo: analisis_total.py
# Proyecto: Análisis de tráfico en Dublín
# ============================================================

# 1) Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import folium
import networkx as nx

# ------------------------------------------------------------
# 2) Cargar datos
# ------------------------------------------------------------
df = pd.read_csv("traffic_flow.csv")
df["DateTime"] = pd.to_datetime(df["DateTime"], dayfirst=True)

# Tráfico total cada 5 min (sumando todos los sensores)
df["Total_5min"] = df.iloc[:, 1:].sum(axis=1)

# Info de sensores (para el mapa)
info = pd.read_csv("counter_information.csv")

# Matrices de red
adj = pd.read_csv("adj_matrix.csv", index_col=0)
dist = pd.read_csv("distances.csv", index_col=0)

# ------------------------------------------------------------
# 3) Análisis temporal (en el tiempo)
# ------------------------------------------------------------
df["Fecha"] = df["DateTime"].dt.date
df["Hora"] = df["DateTime"].dt.hour
df["DiaSemana"] = df["DateTime"].dt.day_name(locale="es_ES")  # Lunes, Martes...
df["Mes"] = df["DateTime"].dt.month

# A) Tráfico por día
trafico_diario = df.groupby("Fecha")["Total_5min"].sum()
trafico_diario.plot(figsize=(12,4), title="Tráfico total por día")
plt.show()

# B) Promedio por día de la semana
promedio_semana = df.groupby("DiaSemana")["Total_5min"].mean()
promedio_semana.plot(kind="bar", title="Promedio por día de la semana")
plt.show()

# C) Promedio por hora
promedio_hora = df.groupby("Hora")["Total_5min"].mean()
promedio_hora.plot(title="Promedio por hora del día")
plt.show()

# D) Promedio por mes
promedio_mes = df.groupby("Mes")["Total_5min"].mean()
promedio_mes.plot(kind="bar", title="Promedio por mes")
plt.show()

# ------------------------------------------------------------
# 4) Detección de anomalías
# ------------------------------------------------------------
# Uso los días: si un día está muy arriba o muy abajo del promedio,
# lo marcamos como "anómalo".

media = trafico_diario.mean()
desv = trafico_diario.std()

anomalos = trafico_diario[
    (trafico_diario > media + 2*desv) | 
    (trafico_diario < media - 2*desv)
]

print("\n⚠️ Días anómalos (muy raro tráfico):")
print(anomalos)

# Graficar con anomalías en rojo
plt.figure(figsize=(12,4))
plt.plot(trafico_diario.index, trafico_diario.values, label="Normal")
plt.scatter(anomalos.index, anomalos.values, color="red", label="Anómalo")
plt.title("Tráfico diario con anomalías")
plt.legend()
plt.show()

# ------------------------------------------------------------
# 5) Predicción simple (media móvil)
# ------------------------------------------------------------
# Una media móvil es un promedio que se va moviendo día a día,
# sirve como predicción sencilla.
prediccion = trafico_diario.rolling(window=7).mean()  # promedio de 7 días

plt.figure(figsize=(12,4))
plt.plot(trafico_diario.index, trafico_diario.values, label="Real")
plt.plot(prediccion.index, prediccion.values, label="Predicción (media móvil 7d)", color="orange")
plt.title("Predicción simple con medias móviles")
plt.legend()
plt.show()

# ------------------------------------------------------------
# 6) Análisis espacial (en el mapa)
# ------------------------------------------------------------
trafico_por_sensor = df.iloc[:, 1:].sum()
info["Total_Traffic"] = trafico_por_sensor.values

m = folium.Map(location=[53.3498, -6.2603], zoom_start=12)
for _, row in info.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        popup=f"Sensor {row['Index']} - {row['Total_Traffic']} vehículos",
        color="red", fill=True, fill_opacity=0.7
    ).add_to(m)
m.save("mapa_sensores.html")
print("✅ Mapa guardado en 'mapa_sensores.html'")

# ------------------------------------------------------------
# 7) Análisis de la red
# ------------------------------------------------------------
G = nx.from_pandas_adjacency(adj)

# Sensores más importantes
centralidad = nx.degree_centrality(G)
print("\n🔑 Sensores más importantes (top 5):")
print(sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5])

# Ejemplo: camino más corto entre dos sensores
camino = nx.shortest_path(G, source="0", target="10")
print("\n➡️ Camino más corto entre sensor 0 y 10:", camino)
