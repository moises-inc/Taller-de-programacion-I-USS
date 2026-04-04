Proceso Ejercicio_3
	// Ejercicio 3: Control de stock en bodega
	// Se registran productos vendidos durante el día. Cada venta reduce el stock. El sistema debe
	// detenerse cuando el stock llegue a 0.
	Definir productos_vendidos, stock Como Entero;
	Escribir '--- Control de stock ---';
	Escribir 'Ingrese stock del día: ';
	Leer stock;
	Mientras stock<>0 Hacer
		Escribir 'Ingrese cantidad de productos vendidos el día de hoy: ';
		Leer productos_vendidos;
		stock <- stock-productos_vendidos;
		Si stock==0 Entonces
			Escribir 'Se acacó el stock del día';
		FinSi
	FinMientras
FinProceso
