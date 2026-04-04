Proceso Ejercicio_5
	// Ejercicio 5: Control de asistencia
	// Un profesor registra asistencia de estudiantes (Presente o Ausente). El proceso termina
	// cuando ya no hay más estudiantes. Mostrar totales.
	Definir estudiantes_totales, estudiantes_presentes, estudiantes_ausentes, i Como Entero;
	Definir asistencia Como Cadena;
	estudiantes_ausentes <- 0;
	estudiantes_presentes <- 0;
	Escribir '--- Control de asistencia ---';
	Escribir 'Ingrese cantidad de estudiantes: ';
	Leer estudiantes_totales;
	Para i<-1 Hasta estudiantes_totales Con Paso 1 Hacer
		Escribir '¿Estudiante ', i, ' presente o ausente ?';
		Leer asistencia;
		Si asistencia=='presente' O asistencia=='Presente' Entonces
			estudiantes_presentes <- estudiantes_presentes+1;
		SiNo
			Si asistencia=='ausente' O asistencia=='Ausente' Entonces
				estudiantes_ausentes <- estudiantes_ausentes+1;
			FinSi
		FinSi
	FinPara
	Escribir 'La cantidad de estudiantes es: ', estudiantes_totales;
	Escribir 'La cantidad de estudiantes presentes es: ', estudiantes_presentes;
	Escribir 'La cantidad de estudiantes ausentes es: ', estudiantes_ausentes;
FinProceso
