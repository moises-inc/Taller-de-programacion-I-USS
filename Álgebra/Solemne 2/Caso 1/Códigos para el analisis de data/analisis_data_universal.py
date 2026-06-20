import pandas as pd
import os

print("=== SCRIPT 1: LIMPIEZA Y CONSOLIDACIÓN DE DATOS ===")
codigo_estacion = input("Por favor, ingresa el código de la estación meteorológica (ej. 10440000): ").strip()

archivo_tmax = 'tmax_cr2met_day.csv'
archivo_tmin = 'tmin_cr2met_day.csv'

# Para Jupyter, detectamos el directorio de trabajo actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_tmax = os.path.join(directorio_actual, archivo_tmax)
ruta_tmin = os.path.join(directorio_actual, archivo_tmin)

try:
    print(f"Cargando datos de la estación {codigo_estacion}...")
    df_tmax = pd.read_csv(ruta_tmax, low_memory=False)
    df_tmin = pd.read_csv(ruta_tmin, low_memory=False)
    
    # Extraer columnas y renombrar
    df_tmax = df_tmax[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_max'})
    df_tmin = df_tmin[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_min'})
    
    # Unificar y calcular T_mean
    df_unificado = pd.merge(df_tmax, df_tmin, on='date')
    df_unificado['T_mean'] = (df_unificado['T_max'] + df_unificado['T_min']) / 2
    
    # Filtro de los últimos 5 años
    df_unificado['date'] = pd.to_datetime(df_unificado['date'])
    anio_maximo = df_unificado['date'].dt.year.max()
    anio_minimo = anio_maximo - 4 
    
    df_5_anios = df_unificado[df_unificado['date'].dt.year >= anio_minimo].copy()
    df_5_anios.dropna(inplace=True)
    
    archivo_salida = os.path.join(directorio_actual, f'datos_consolidados_{codigo_estacion}_5anios.csv')
    df_5_anios.to_csv(archivo_salida, index=False)
    
    print(f"✅ ¡Éxito! Datos filtrados desde {anio_minimo} hasta {anio_maximo}.")
    print(f"Archivo guardado como: {archivo_salida}\n")

except FileNotFoundError:
    print(f"❌ Error: No se encontraron los archivos base (tmax_cr2met_day.csv o tmin). Verifica que estén en {directorio_actual}")
except KeyError:
    print(f"❌ Error: El código de estación {codigo_estacion} no existe en la base de datos o está mal escrito.")
