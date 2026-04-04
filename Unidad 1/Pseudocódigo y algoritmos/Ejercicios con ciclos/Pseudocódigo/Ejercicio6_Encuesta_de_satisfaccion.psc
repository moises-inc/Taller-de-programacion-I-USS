Proceso Ejercicio6_Encuesta_de_satisfaccion
	// Ejercicio 6: Encuesta de satisfacción
	// Se registran notas de clientes (1 a 7). El proceso termina cuando se ingresa 0. Mostrar
	// promedio, cantidad de respuestas y evaluaciones bajo 4.
	Definir notas, promedio, cantidad_respuestas, notas_azules, notas_rojas, cantidad_clientes, contador, suma_notas Como Real;
	Definir validador Como Logico;
	Escribir '--- Encuesta de satisfacción ---';
	validador <- Falso;
	contador <- 0;
	notas_azules <- 0;
	notas_rojas <- 0;
	suma_notas <- 0;
	Mientras validador==Falso Hacer
		contador <- contador+1;
		Escribir 'Ingrese nota de cliente ', contador, ' o ingrese 0 para detener el programa';
		Leer notas;
		Si notas==0 Entonces
			validador <- Verdadero;
		SiNo
			Si notas>=4 Entonces
				notas_azules <- notas_azules+1;
			SiNo
				Si notas>0 Y notas<4 Entonces
					notas_rojas <- notas_rojas+1;
				FinSi
			FinSi
		FinSi
		suma_notas <- suma_notas+notas;
	FinMientras
	promedio <- suma_notas/(contador-1);
	Escribir 'Total de trabajadores es: ', contador-1;
	Escribir 'El promedio de notas es: ', promedio;
	Escribir 'Las cantidad de notas sobre 4 son: ', notas_azules;
	Escribir 'La cantidad de notas bajo 4 son: ', notas_rojas;
FinProceso
