# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd

# Definimos la ruta donde estará guardado el dataset dentro del repositorio
ruta_dataset = 'src/yellow_tripdata_2026-07.parquet'

print("--- Iniciando análisis del dataset de viajes ---")

# Lectura del dataset
df = pd.read_parquet(ruta_dataset)

# Cantidad de registros
cant_reg = df.shape[0]
print(f"Registros: {cant_reg}")

# Cantidad de columnas
cantidad_columnas = df.shape[1]
print(f"Cantidad de columnas: {cantidad_columnas}")

# Tamaño del archivo
# Obtiene el tamaño en bytes y lo convierte a Megabytes (MB)
tamaño_bytes = os.path.getsize(ruta_dataset)
tamaño_mb = tamaño_bytes / (1024 * 1024)
print(f"Tamaño del archivo en disco: {tamaño_mb:.2f} MB")

# Tipos de datos
tipos = df.dtypes
print("\nTipos de datos por columna:")
print(tipos)

# Valores faltantes por columna
faltantes = df.isna().sum()
print("\nValores faltantes por columna:")
print(faltantes)

# Variables Disponibles
# (Ya no es necesario volver a leer el dataframe aquí, usamos el que ya está cargado)
print("\nVariables disponibles:")
for variable in df.columns:
    print(f"- {variable}")