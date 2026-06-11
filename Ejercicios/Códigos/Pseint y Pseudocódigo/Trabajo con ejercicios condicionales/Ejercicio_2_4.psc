Proceso Ejercicio_2_4
	Definir total, nuevo_total Como Real;
	Escribir 'Ingrese total de la compra: ';
	Leer total;
	Si total>40000 Entonces
		nuevo_total <- total*0.9;
		Escribir 'El nuevo precio a pagar es ', nuevo_total;
	SiNo
		Si total>100000 Entonces
			nuevo_total <- total*0.8;
			Escribir 'El precio a pagar es ', nuevo_total;
		SiNo
			Escribir 'No hay descuento';
		FinSi
	FinSi
FinProceso
