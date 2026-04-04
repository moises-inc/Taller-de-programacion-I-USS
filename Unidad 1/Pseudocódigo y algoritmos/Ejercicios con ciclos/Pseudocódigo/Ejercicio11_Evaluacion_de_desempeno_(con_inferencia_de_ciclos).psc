Proceso Ejercicio_11
	
	// Una empresa realizó una evaluación de desempeño a sus trabajadores.
	// Antes de comenzar el registro, se solicita ingresar la cantidad total de trabajadores evaluados.
	// Luego, para cada trabajador, se debe ingresar su nota (de 1 a 7).
	// El sistema debe:
		// Mostrar cuántos trabajadores aprobaron (nota >= 4)
		// Mostrar cuántos reprobaron
		// Mostrar el promedio general de las notas
	// El estudiante debe inferir que:
		// La cantidad de iteraciones depende de la cantidad de trabajadores
		// Debe usar un Para desde 1 hasta N
		// Usar Si para clasificar
	
	
	Definir cantidad_trabajadores, trabajadores_aprobados, trabajadores_reprobados, contador, i Como Entero;
	Definir nota_trabajador, promedio_general, suma_nota Como Real;
	
	Escribir "--- Evaluación de Trabajadores ---";
	contador <- 0;
	trabajadores_aprobados <- 0;
	trabajadores_reprobados <- 0;
	suma_nota <- 0 ;
	
	Escribir "Ingrese cantidad de trabajadores a evaluar: ";
	Leer cantidad_trabajadores;
	
	Para i<- 1 Hasta cantidad_trabajadores Con Paso 1 Hacer
		Escribir "Ingrese nota de trabajador: ", i;
		Leer nota_trabajador;
		
		Si nota_trabajador >= 4 Entonces
			trabajadores_aprobados <- trabajadores_aprobados + 1;
		Sino
			trabajadores_reprobados <- trabajadores_reprobados +1; 
			
		FinSi
		
		suma_nota <- nota_trabajador + suma_nota;
	FinPara
	
	
	promedio_general <- suma_nota / cantidad_trabajadores;
	
	Escribir "--- Resultados de evaluación"; 
	
	Escribir "La cantidad de trabajadores aprobados es: ", trabajadores_aprobados;
	Escribir "La cantidad de trabajadores reprobados es: ", trabajadores_reprobados;
	Escribir "El promedio general es: ", promedio_general;
	
	Si trabajadores_aprobados > trabajadores_reprobados Entonces
		Escribir "Felicidades, la mayoría de trabajadores aprobó.";
	SiNo
		Escribir "Lo siento, la mayoría de trabajadores reprobaron"; 
	FinSi
	
	
FinProceso
