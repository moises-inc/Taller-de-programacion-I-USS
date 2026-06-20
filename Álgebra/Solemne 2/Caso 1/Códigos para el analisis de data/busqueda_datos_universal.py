import pandas as pd
import os

print("=== SCRIPT 2: CÁLCULO DE CARDINALIDADES ===")
codigo_estacion = input("Ingresa el código de la estación a analizar (ej. 10440000): ").strip()
zona_geografica = input("Ingresa la zona geográfica (Norte, Centro o Sur): ").strip()

directorio_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = f'datos_consolidados_{codigo_estacion}_5anios.csv'
ruta_datos = os.path.join(directorio_actual, nombre_archivo)

try:
    df = pd.read_csv(ruta_datos)
    
    # Conjuntos Lógicos
    cond_A = df['T_max'] > 30
    cond_B = df['T_min'] < 10
    cond_C = (df['T_mean'] >= 18) & (df['T_mean'] <= 22)
    
    resultados = {
        "Estación": codigo_estacion,
        "Zona": zona_geografica,
        "A": cond_A.sum(),
        "B": cond_B.sum(),
        "C": cond_C.sum(),
        "AnB": (cond_A & cond_B).sum(),
        "AnC": (cond_A & cond_C).sum(),
        "BnC": (cond_B & cond_C).sum(),
        "AnBnC": (cond_A & cond_B & cond_C).sum()
    }
    
    print("\n" + "-" * 50)
    print(f" RESULTADOS: ESTACIÓN {codigo_estacion} ({zona_geografica.upper()}) ")
    print("-" * 50)
    for clave, valor in resultados.items():
        print(f"{clave:<10}: {valor}")
    print("-" * 50)
    
    # Guardar en CSV
    df_resultados = pd.DataFrame([resultados])
    nombre_salida = f'resultados_cardinalidad_{codigo_estacion}.csv'
    df_resultados.to_csv(os.path.join(directorio_actual, nombre_salida), index=False)
    print(f"✅ Tabla exportada exitosamente como: {nombre_salida}")

except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'. Ejecuta el Script 1 primero para esta estación.")
