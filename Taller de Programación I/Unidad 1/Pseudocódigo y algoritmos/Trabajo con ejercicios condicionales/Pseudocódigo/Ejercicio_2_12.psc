Proceso Ejercicio_2_12
	Definir temperatura Como Real;
	Escribir 'Ingresa la temperatura en Celsius: ';
	Leer temperatura;
	Si temperatura<0 Entonces
		Escribir 'Temperatura bajo cero';
	SiNo
		Si temperatura<20 Entonces
			Escribir 'Temperatura fría';
		SiNo
			Si temperatura<30 Entonces
				Escribir 'Temperatura templada';
			SiNo
				Escribir 'Temperatura caliente';
			FinSi
		FinSi
	FinSi
FinProceso
