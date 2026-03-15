Proceso Ejercicio_2_11
	Definir dias Como Entero;
	Definir subtotal, total Como Real;
	Escribir 'Ingresa la cantidad de días que va a alquilar el auto: ';
	Leer dias;
	subtotal <- dias*50000;
	Si dias>7 Entonces
		total <- subtotal*0.75;
		Escribir 'El total a pagar es ', total;
	SiNo
		Si (dias>3) Y (dias<7) Entonces
			total <- subtotal*0.9;
			Escribir ' El total a pagar es ', total;
		SiNo
			Escribir 'No hay descuento, el total es ', total;
		FinSi
	FinSi
FinProceso
