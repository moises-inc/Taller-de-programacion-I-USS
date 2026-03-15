Proceso Ejercicio_2_13
	Definir patente Como Cadena;
	Definir horas, tarifa Como Real;
	Escribir 'Ingresa tu patente: ';
	Leer patente;
	Escribir 'Ingresa las horas estacionado: ';
	Leer horas;
	Si horas<=2 Entonces
		tarifa <- 2000;
		Escribir 'El auto con patente ', patente, ' debe pagar ', tarifa;
	SiNo
		Si horas<=5 Entonces
			tarifa <- 3500;
			Escribir 'El auto con patente ', patente, ' debe pagar ', tarifa;
		SiNo
			tarifa <- 5000;
			Escribir 'El auto con patente ', patente, ' debe pagar ', tarifa;
		FinSi
	FinSi
FinProceso
