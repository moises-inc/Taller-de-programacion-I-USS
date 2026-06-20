# --- DATOS DE PRUEBA GLOBALES (Ahora sí se pueden importar) ---
mock_estudiantes_limpios = {
    "12345678-9": {"Nombre": "Moisés", "Malla": "2024", "Estado_Academico": "Al día"},
    "98765432-1": {"Nombre": "Alumno Atrasado", "Malla": "2019", "Estado_Academico": "Atrasado"}
}
    
mock_asignaturas_limpias = {
    "FP2001": {"Nombre": "Big Data", "Malla": "2024", "Tipo": "Teórico", "Profesor_ID": "P02", "Cupos": 2},
    "FP1003": {"Nombre": "Bases de Datos", "Malla": "2019", "Tipo": "Teórico", "Profesor_ID": "P03", "Cupos": 0}
}


class MotorDecisionesAcademicas:
    def __init__(self, df_estudiantes, df_asignaturas):
        # En producción, estos serán los DataFrames limpios que prepare Fernando
        self.db_estudiantes = df_estudiantes
        self.db_asignaturas = df_asignaturas

    def buscar_estudiante(self, rut):
        # Simula la búsqueda del estudiante en la base de datos
        estudiante = self.db_estudiantes.get(rut)
        if not estudiante:
            return None
        return estudiante

    def buscar_asignatura(self, nrc):
        # Simula la búsqueda de la asignatura
        asignatura = self.db_asignaturas.get(nrc)
        if not asignatura:
            return None
        return asignatura

    def validar_cupos(self, nrc):
        asignatura = self.buscar_asignatura(nrc)
        cupos_actuales = asignatura['Cupos']
        
        if cupos_actuales > 0:
            return True, cupos_actuales
        else:
            return False, 0

    def evaluar_solicitud(self, rut, nrc):
        estudiante = self.buscar_estudiante(rut)
        asignatura = self.buscar_asignatura(nrc)

        # 1. Validación de Identidad
        if not estudiante or not asignatura:
            return "Error: Estudiante o NRC no encontrado en los registros."

        # 2. Validación de Malla (2019 vs 2024)
        malla_estudiante = estudiante['Malla']
        malla_asignatura = asignatura['Malla']
        
        if malla_asignatura != "Ambas" and malla_estudiante != malla_asignatura:
            return f"Rechazado: La asignatura ({malla_asignatura}) no corresponde a tu malla actual ({malla_estudiante}). Requiere sección especial."

        # 3. Validación de Estado Académico ("Al día" vs "Atrasado")
        estado = estudiante['Estado_Academico']
        
        if estado == "Atrasado":
            # Aquí irían las lógicas complejas a futuro:
            # - Verificar prerrequisitos específicos
            # - Verificar topes de horario
            # Por ahora, para el Piloto Cero, requerirá revisión manual si hay tope.
            pass 

        # 4. Validación Final de Cupos y Condicionales Adicionales
        hay_cupo, cupos_restantes = self.validar_cupos(nrc)
        
        if not hay_cupo:
            return "Rechazado: La sección solicitada no cuenta con cupos disponibles."
        
        # Si hay cupo, se evalúa la regla del Co-requisito (Teoría y Práctica con mismo profe)
        tipo_asignatura = asignatura['Tipo']
        if tipo_asignatura == "Práctico":
            # Lógica simulada: Verificar si ya tiene inscrita la teoría con el mismo Profesor_ID
            # if no_tiene_teoria_emparejada:
            #     return "Rechazado: Debes inscribir la sección teórica con el mismo docente antes de tomar la práctica."
            pass

        # 5. Aprobación y Actualización de Cupo Temporal
        # Restamos 1 al cupo local para evitar la Condición de Carrera durante el día
        self.db_asignaturas[nrc]['Cupos'] -= 1
        
        return f"Pre-Aprobado. Solicitud encolada para Jefatura. (Cupos restantes locales: {self.db_asignaturas[nrc]['Cupos']})"

# --- Entorno de Pruebas ---
# --- ENTORNO DE PRUEBAS LOCAL ---
if __name__ == "__main__":
    # Aquí ahora SOLO dejamos la inicialización y los prints de prueba
    motor = MotorDecisionesAcademicas(mock_estudiantes_limpios, mock_asignaturas_limpias)

    print("Prueba 1:", motor.evaluar_solicitud("12345678-9", "FP2001"))
    print("Prueba 2:", motor.evaluar_solicitud("12345678-9", "FP2001"))