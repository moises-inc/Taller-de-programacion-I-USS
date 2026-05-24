Proceso Ejercicio12
	
	// Una fábrica registra su producción durante una jornada de trabajo.
	// Antes de comenzar, el supervisor indica cuántas horas durará la jornada.
	// Luego, por cada hora, se debe ingresar la cantidad de productos fabricados.
	// El sistema debe:
		// Mostrar el total producido en la jornada
		// Indicar cuántas horas la producción fue baja (menos de 50 unidades)
		// Indicar cuántas horas la producción fue alta (100 o más)
	// El estudiante debe inferir que:
		// La cantidad de ciclos depende de las horas de la jornada
		// Debe usar un Para controlado por ese valor
		// Usar Si para clasificar producción
	
	
	Definir duracion_jornada, productos_fabricados, total_producido, i, suma_productos Como Entero;
	
	suma_productos <- 0;
	
	Escribir "--- Registro de produción ---";
	
	Escribir "Ingrese cuántas horas durará la jornada: ";
	Leer duracion_jornada;
	
	Para i<- 1 Hasta duracion_jornada Con Paso 1 Hacer
		
		Escribir "Ingrese cantidad de productos fabricados en ", i, " hora: ";
		Leer productos_fabricados;
		suma_productos <- productos_fabricados + suma_productos;
		
	FinPara
	
	Si suma_productos >= 100 Entonces
		Escribir "La produción fué alta, la produción total fué: ", suma_productos;
	Sino 
		Escribir "La producción fué baja, la producción total fué: ", suma_productos;
	FinSi
	
FinProceso
