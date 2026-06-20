import pandas as pd
import random

# 1. Generar Tabla de Estudiantes (Con RUTs sucios y diferentes mallas)
def generar_estudiantes(cantidad=50):
    nombres = ["Juan", "Camila", "Fernando", "Moisés", "Ana", "Pedro", "Sofía", "Luis", "Valentina", "Diego"]
    apellidos = ["Pérez", "González", "Tapia", "Romero", "Aravena", "Soto", "Contreras", "Silva", "Martínez"]
    
    estudiantes = []
    for _ in range(cantidad):
        # Generador de RUTs con formatos inconsistentes (Data sucia intencional)
        rut_base = f"{random.randint(10, 25)}{random.randint(100, 999)}{random.randint(100, 999)}"
        digito = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K", "k"])
        
        formato_rut = random.choice([
            f"{rut_base}-{digito}",                # Limpio: 12345678-9
            f"{rut_base[:2]}.{rut_base[2:5]}.{rut_base[5:]}-{digito}", # Con puntos: 12.345.678-9
            f"{rut_base}{digito}",                 # Sin guion: 123456789
            f"{rut_base}- {digito}"                # Con espacio extra: 12345678- 9
        ])
        
        estudiantes.append({
            "RUT": formato_rut,
            "Nombre": f"{random.choice(nombres)} {random.choice(apellidos)}",
            "Malla": random.choice(["2019", "2024"]),
            "Estado_Academico": random.choice(["Al día", "Atrasado"]),
            "Anio_Ingreso": random.choice([2019, 2020, 2021, 2022, 2023, 2024])
        })
    
    df_estudiantes = pd.DataFrame(estudiantes)
    df_estudiantes.to_csv("mock_estudiantes.csv", index=False)
    print("✅ Archivo 'mock_estudiantes.csv' generado.")

# 2. Generar Tabla de Asignaturas de Formación Profesional
def generar_asignaturas():
    asignaturas = [
        {"NRC": "FP1001", "Nombre": "Desarrollo TI (Teoría)", "Malla": "Ambas", "Tipo": "Teórico", "Profesor_ID": "P01", "Cupos": 30},
        {"NRC": "FP1002", "Nombre": "Desarrollo TI (Práctica)", "Malla": "Ambas", "Tipo": "Práctico", "Profesor_ID": "P01", "Cupos": 30},
        {"NRC": "FP2001", "Nombre": "Big Data", "Malla": "2024", "Tipo": "Teórico", "Profesor_ID": "P02", "Cupos": 25},
        {"NRC": "FP1003", "Nombre": "Bases de Datos", "Malla": "2019", "Tipo": "Teórico", "Profesor_ID": "P03", "Cupos": 20},
        {"NRC": "FP1004", "Nombre": "Bases de Datos (Convalidable)", "Malla": "Ambas", "Tipo": "Teórico", "Profesor_ID": "P03", "Cupos": 15},
    ]
    df_asignaturas = pd.DataFrame(asignaturas)
    df_asignaturas.to_csv("mock_asignaturas.csv", index=False)
    print("✅ Archivo 'mock_asignaturas.csv' generado.")

# Ejecutar funciones
if __name__ == "__main__":
    print("Iniciando generación de base de datos ficticia para Hermes Analytics...")
    generar_estudiantes()
    generar_asignaturas()
    print("Proceso completado. Listo para limpieza en Pandas.")