Proceso Ejercicio_2_15
	Definir forma_pago Como Cadena;
	Definir total Como Real;
	Escribir 'Ingresa forma de pago (efectivo, crédito o débito): ';
	Leer forma_pago;
	Si forma_pago=='efectivo' Entonces
		total <- 80000-5000;
		Escribir 'El total a pagar es ', total;
	SiNo
		Si forma_pago=='crédito' Entonces
			total <- 80000+3000;
			Escribir 'El total a pagar es ', total;
		SiNo
			Si forma_pago=='débito' Entonces
				total <- 80000;
				Escribir 'El total a pagar es ', total;
			SiNo
				Escribir 'Forma de pago incorrecta';
			FinSi
		FinSi
	FinSi
FinProceso
