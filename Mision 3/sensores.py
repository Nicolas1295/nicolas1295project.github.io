import pandas as pd
import folium

# -----------------------------
# 1. Cargar archivos
# -----------------------------
df_trafico = pd.read_csv("traffic_flow.csv")
df_info = pd.read_csv("counter_information.csv")

# -----------------------------
# 2. Preparar dataset de tráfico
# -----------------------------
# Convertir columna de tiempo
df_trafico["DateTime"] = pd.to_datetime(df_trafico["DateTime"], dayfirst=True)

# Calcular tráfico total por sensor (sumando todas las filas por cada columna de sensores)
trafico_por_sensor = df_trafico.iloc[:, 1:].sum()

# -----------------------------
# 3. Unir con coordenadas
# -----------------------------
df_info["Total_Traffic"] = trafico_por_sensor.values

# -----------------------------
# 4. Crear mapa interactivo
# -----------------------------
m = folium.Map(location=[53.3498, -6.2603], zoom_start=12)

for _, row in df_info.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        popup=f"Sensor {row['Index']} - Tráfico: {row['Total_Traffic']}",
        color="red",
        fill=True,
        fill_opacity=0.7
    ).add_to(m)

m.save("mapa_sensores.html")
print("✅ Mapa creado: abre 'mapa_sensores.html' en tu navegador")
print(df_info.head())
