# ------------------------------------------------------------
# archivo: analisis_sensor0.py
# Propósito: leer un CSV con flujo de tráfico, filtrar 01/01/2021
#           y graficar la serie temporal del sensor "0".
# Comentarios: todo está explicado paso a paso abajo.
# ------------------------------------------------------------

# 1) IMPORTAR LIBRERÍAS
import pandas as pd
# - 'import' es la sentencia que carga un módulo (biblioteca) en memoria.
# - 'pandas' es el nombre del módulo.
# - 'as pd' crea un alias llamado 'pd' para usar la librería con menos escritura.
#   (usar 'pd' es una convención muy común).

import matplotlib.pyplot as plt
# - 'matplotlib.pyplot' es el submódulo para crear gráficos.
# - 'as plt' crea el alias 'plt' (convención común).

# 2) LEER EL ARCHIVO CSV
df = pd.read_csv("traffic_flow.csv")
# - ' ahí df se convirtió en un DataFrame.
# - 'Un DataFrame en pandas es como una tabla de Excel en memoria: tiene filas y columnas.
# - 'pd.read_csv' es una función que abre un archivo CSV y devuelve un DataFrame.
# - "traffic_flow.csv" es un string literal: el nombre del archivo (ruta relativa).
# - '=' (operador de asignación) guarda el resultado en la variable 'df'.
# - 'df' es una variable que típicamente referimos como "DataFrame" (tabla).

# 3) INVESTIGAR RÁPIDO (OPCIONAL, ÚTIL PARA APRENDER)
print("=== df.head() ===")
print(df.head())
# - df.head() devuelve las primeras 5 filas del DataFrame.
# - print(...) imprime texto en la terminal.

print("\n=== df.info() ===")
print(df.info())
# - df.info() muestra información de columnas, tipos y nulos.
# - ¡Nota: print(df.info()) imprime 'None' después porque df.info()
#         ya imprime por sí mismo; lo dejo así para que veas el comportamiento.

# 4) CONVERTIR LA COLUMNA DateTime A TIPO FECHA/HORA
df["DateTime"] = pd.to_datetime(df["DateTime"], dayfirst=True)
# - df["DateTime"] -> selección por etiqueta de columna (devuelve una Series).
# - pd.to_datetime(...) -> función que convierte strings a objetos datetime64.
# - dayfirst=True -> parámetro keyword (nombre=valor) que indica formato día/mes/año.
# - Con dayfirst=True = 1 de febrero de 2021. con dayfirst=False = 2 de enero de 2021.
# - El resultado (Series de datetimes) se asigna de nuevo a df["DateTime"].
# - Nota: usamos comillas "DateTime" porque el nombre de la columna es texto.

# 5) CREAR UNA MÁSCARA BOOLEANA PARA EL PRIMER DÍA
# Explicación por partes:
# - df["DateTime"].dt.date : toma la Series datetime y obtiene sólo la parte 'date'
# - pd.to_datetime("2021-01-01").date() : crea un objeto datetime y pide su .date()
# - La comparación '==' produce una Series booleana (True/False por fila).
mask_primer_dia = df["DateTime"].dt.date == pd.to_datetime("2021-01-01").date()
# - '=' asigna la Series booleana a la variable mask_primer_dia.

# 6) FILTRAR EL DATAFRAME USANDO LA MÁSCARA
primer_dia = df[mask_primer_dia]
# - df[mask_primer_dia] -> indexación booleana: devuelve sólo las filas donde
#   mask_primer_dia es True.
# - Asignamos el DataFrame resultante a la variable 'primer_dia'.

# 7) (OPCIONAL) Revisar cuántas filas quedaron y qué columnas
print("\nFilas del primer día:", primer_dia.shape[0])   # shape[0] = número de filas
print("Columnas disponibles:", list(primer_dia.columns))  # lista de nombres de columna

# 8) GRAFICAR: serie temporal del sensor "0" para 01/01/2021
#    (recuerda: en el CSV el encabezado del sensor es '0' como texto)
plt.figure(figsize=(12, 6))
# - plt.figure(...) crea una figura nueva.
# - figsize=(12,6) es una tupla que indica el tamaño en pulgadas (ancho, alto).

# plt.plot(x, y, ...) -> x: valores eje X, y: valores eje Y
plt.plot(
    primer_dia["DateTime"],  # eje X: la columna de fechas (Series datetime)
    primer_dia["0"],         # eje Y: la columna '0' (conteos)//NOTA: '0' es texto
    label="Sensor 0",        # etiqueta para la leyenda (keyword argument)
    color="blue"             # color de la línea (keyword argument)
)
# - cada argumento dentro de plt.plot(...) está separado por coma ','.
# - los parámetros con 'nombre=valor' son keyword arguments y pueden venir en cualquier orden.

# 9) TITULOS Y ETIQUETAS
plt.title("Tráfico del Sensor 0 - 01/01/2021")
# - pone el título de la gráfica.

plt.xlabel("Hora")
# - etiqueta eje X.

plt.ylabel("Vehículos (cada 5 min)")
# - etiqueta eje Y.

# 10) ROTAR LAS ETIQUETAS DEL EJE X PARA QUE NO SE SOLAPEN
plt.xticks(rotation=45)
# - plt.xticks modifica las marcas (ticks) del eje X.
# - rotation=45 rota las etiquetas 45 grados (keyword argument).

# 11) LEYENDA Y CUADRÍCULA
plt.legend()   # muestra la leyenda con la label especificada en plt.plot()
plt.grid(True) # activa la cuadrícula; True es booleano (verdadero)

# 12) MOSTRAR LA GRÁFICA
plt.show()
# - plt.show() abre la ventana con la gráfica cuando ejecutas el script desde la terminal.
# - En Jupyter Notebook a veces no hace falta, pero en script sí.
