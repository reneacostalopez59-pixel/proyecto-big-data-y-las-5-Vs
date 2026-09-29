# Diagnóstico de un caso de Big Data: Taxis y Limusinas de Nueva York

## Descripción del Proyecto
Este repositorio contiene el análisis de un conjunto de datos relacionado con estadisticas y tarifas de viajes de los taxis amarillos (Yellow Taxis) de Nueva York, desarrollado como proyecto para la asignatura de Fundamentos de Big Data.

## Las 5 V's del Big Data en Taxis y Limusinas de NYC
Para este caso de estudio, identificamos las siguientes características:

*   Volumen: La organización de Taxis y Limosinas de Nueva York guarda todos los datos y registros que se generan con cada uno de los viajes en la ciudad. Nuestra base de interes es la sección de Taxis Amarillos. Dado que en la ciudad de nueva york se hacen aproximadamente 300 mil viajes diarios en taxis amarillos.
*   Velocidad: Los datos se actualizan al instante, en el momento que un usuario solicita un taxi o sube a uno, en tiempos de viaje, en la ubicación de destino, en la tarifa que incrementa conforme avanza el kilometraje, etc. Sumado a que estos datos se generan a traves de todos los taxis amarillos de Nueva York, la velocidad a la que se generan o actualizan estos datos es brutal. Para procesar y guardar estos datos se requiere un sistema eficiente y óptimo para este tipo de generación de datos.
*   Variedad: La organización guarda datos numericos como tarifas, recorridos, tiempos de viaje, tiempo de espera; Datos geográficos, como destino, ubicación, origen, tarifas itemizadas, y otros datos, como reportes a los choferes, numero de unidad, matricula, marca, modelo, y fechas.
*   Veracidad: Dado que estos datos son calculados y proporcionados por cada taxi en el momento, generalmente son datos verdaderos, sin embargo, no esta exenta de errores, puede haber un viaje programado por error, donde no haya ningun usuario y ningun destino, pero aún así se esta actualizando una tarifa de viaje. Sin embargo, en promedio, todos los datos que se registran, son correctos.
*   Valor: Se puede atender problemas de eficiencia en rutas, ubicar las zonas donde se solicitan más taxis, la tarifa promedio de los usuarios, las distancias promedio de los recorridos, las preferencias de los usuarios, los reportes a choferes, saber que unidad está en uso, y tener un mapa general de viajes y estadísticas de los taxis amarillos en Nueva York.

(El diagrama visual de estas 5 V's se encuentra en la ruta docs/5vs-diagrama.png)

---

## Instrucciones de Instalación
Para que el proyecto pueda ejecutarse en otro equipo siguiendo únicamente las instrucciones de este repositorio, realiza los siguientes pasos[cite: 2]:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/reneacostalopez59-pixel/proyecto-big-data-y-las-5-Vs.git](https://github.com/reneacostalopez59-pixel/proyecto-big-data-y-las-5-Vs.git)
    cd proyecto-big-data-y-las-5-Vs
    ```

2.  **Instalar las dependencias:**
    Ejecuta el siguiente comando para instalar las librerías necesarias (`pandas`, `numpy`, `pyarrow`)[cite: 3, 4]:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Obtener el Dataset:**
    Por restricciones de almacenamiento, el dataset no se sube a GitHub[cite: 3]. 
    * Descarga el archivo original `yellow_tripdata_2026-07.parquet`.
    * Colócalo exactamente dentro de la carpeta `data/` del proyecto sin cambiarle el nombre[cite: 3].

---

## 4. Instrucciones de Ejecución
Con el entorno preparado y el dataset ubicado en la carpeta `data/`[cite: 3], ejecuta el programa de análisis desde la raíz del proyecto usando el siguiente comando en tu terminal[cite: 2]:

```bash
python src/main.py

---

## 5. Explicación de los Resultados
Al ejecutar el script de Python, el código lee el archivo `.parquet` y devuelve exitosamente la siguiente información básica requerida sobre el conjunto de datos[cite: 1, 4]:

*   **Cantidad de registros:** El script utiliza la función `.shape[0]` para calcular y mostrar el número total de filas, lo que representa la cantidad exacta de viajes realizados en ese mes[cite: 4].
*   **Cantidad de columnas:** Utilizando `.shape[1]`, se expone el total de campos disponibles por viaje (usualmente 19 columnas para este dataset)[cite: 4].
*   **Tamaño aproximado del dataset:** El código utiliza la librería `os` para calcular el tamaño real del archivo en el disco y lo convierte dinámicamente para imprimir su peso en Megabytes (MB)[cite: 4].
*   **Tipos de datos:** A través de `.dtypes`, el sistema identifica si las columnas son de tipo entero (`int64` para pasajeros), decimal (`float64` para montos y distancias) o temporales (`datetime64` para las horas de los viajes)[cite: 4].
*   **Valores faltantes:** Mediante `.isna().sum()`, el programa realiza un conteo por columna para identificar dónde existen datos nulos o perdidos que requieran limpieza posterior[cite: 4].
*   **Variables disponibles:** Finalmente, un ciclo itera sobre `.columns` para listar todos los nombres de las variables del dataset (como tarifa total, distancia, zonas, etc.)[cite: 4].

*(Las capturas de pantalla de la terminal que demuestran la ejecución exitosa de estos resultados se encuentran guardadas en la carpeta `docs/evidencias/`)*[cite: 2, 3].