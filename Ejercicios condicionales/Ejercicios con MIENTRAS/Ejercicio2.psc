Proceso Ejercicio2
	
	// Ejercicio 2: Registro de ventas del día
	// Un vendedor ingresa los montos de sus ventas hasta que decide terminar (ingresando 0). 
	// El sistema debe calcular el total vendido, cantidad de ventas y promedio
	
	
	Definir total_vendido, promedio, monto_venta Como Real;
	Definir cantidad_ventas Como Entero;
	
	// Inicialización de variables
	total_vendido <- 0;
	cantidad_ventas <- 0;
	
	Escribir "--- Registro de ventas diarias ---";
	
	// Pedimos el primer dato ANTES del bucle para poder evaluarlo
	Escribir "Ingrese monto de la venta (o ingrese 0 para terminar): ";
	Leer monto_venta;
	
	// El bucle se repite MIENTRAS el monto no sea cero
	Mientras (monto_venta <> 0) Hacer
		
		Si (monto_venta > 0) Entonces
            
            // Es un número válido (positivo), así que lo acumulamos y contamos
            total_vendido <- total_vendido + monto_venta;
			// Las variables parten en 0, conforme se ejecuta el ciclo estas variables van aumentando
            cantidad_ventas <- cantidad_ventas + 1;
            
        Sino
            // Es un número negativo, mostramos el error y NO lo sumamos
            Escribir ">> ¡ERROR! El monto no puede ser negativo. Intente nuevamente.";
			// La validación se repite siempre, hasta que se ingrese un número 0 para finalizar el bucle
            
        FinSi
		
		// Volvemos a pedir el monto para la siguiente iteración hasta que monto_venta sea = 0
		Escribir "Ingrese monto de la venta (o ingrese 0 para terminar): ";
		Leer monto_venta;
		
	FinMientras
	
	// Cálculos finales y prevención de errores
	Si (cantidad_ventas > 0) Entonces
		// El denominador no puede ser 0, además, el promedio de ventas no tiene sentido que sea negativo.
		promedio <- total_vendido / cantidad_ventas;
		
		Escribir "--- RESUMEN DEL DÍA ---";
		Escribir "Total vendido: $", total_vendido;
		Escribir "Cantidad de ventas: ", cantidad_ventas;
		Escribir "Promedio por venta: $", promedio;
	Sino
		Escribir "No se registraron ventas en el día.";
	FinSi
	
FinProceso
