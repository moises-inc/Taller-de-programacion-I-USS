Proceso Ejercicio10_Sistema_de_notas
	// Ejercicio 10: Sistema de notas
	// Se ingresan notas hasta ingresar -1. Mostrar promedio final y si el estudiante aprueba o reprueba.
	Definir notas, suma_notas, promedio, estudiantes_aprobados, estudiantes_reprobados, contador Como Real;
	Definir validador Como Logico;
	suma_notas <- 0;
	contador <- 0;
	estudiantes_aprobados <- 0;
	estudiantes_reprobados <- 0;
	validador <- Falso;
	Escribir '--- Sistema de notas ---';
	Mientras validador==Falso Hacer
		contador <- contador+1;
		Escribir 'Ingrese notas de alumno ', contador, ' o ingrese -1 para terminar el registro';
		Leer notas;
		Si notas==-1 Entonces
			validador <- Verdadero;
		SiNo
			Si notas>=4 Entonces
				estudiantes_aprobados <- estudiantes_aprobados+1;
			SiNo
				Si notas>0 Y notas<4 Entonces
					estudiantes_reprobados <- estudiantes_reprobados+1;
				FinSi
			FinSi
		FinSi
		suma_notas <- suma_notas+notas;
	FinMientras
	Escribir 'Los estudiantes aprobados son: ', estudiantes_aprobados;
	Si contador==1 Entonces
		Escribir 'No se redistraron notas';
		Escribir 'El total de estudiantes es: ', contador-1;
		promedio <- 0;
		Escribir 'El promedio es ', promedio;
	SiNo
		Escribir 'El total de estudiantes es: ', contador-1;
		promedio <- suma_notas/(contador-1);
		Escribir 'El promedio es ', promedio;
	FinSi
	Escribir 'Los estudiantes reprobados son: ', estudiantes_reprobados;
FinProceso
