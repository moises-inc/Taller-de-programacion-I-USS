Proceso Ejercicio_2_7
	Definir num_a, num_b, resultado Como Real;
	Definir operacion Como Cadena;
	Escribir 'Ingresa un número a: ';
	Leer num_a;
	Escribir 'Ingresa un número b: ';
	Leer num_b;
	Escribir 'Ingresa una operación a realizar (+, -, *, /): ';
	Escribir 'Ingresa un orden de la operación (ejemplo: a+b, b-a, a/b): ';
	Leer operacion;
	Si (operacion=='a+b') O (operacion=='b+a') Entonces
		resultado <- num_a+num_b;
		Escribir 'El resultado es ', resultado;
	SiNo
		Si (operacion=='a*b') O (operacion=='b*a') Entonces
			resultado <- num_a*num_b;
			Escribir 'El resultado es ', resultado;
		SiNo
			Si operacion=='a-b' Entonces
				resultado <- num_a-num_b;
				Escribir 'El resultado es ', resultado;
			SiNo
				Si operacion=='b-a' Entonces
					resultado <- num_b-num_a;
					Escribir 'El resultado es ', resultado;
				SiNo
					Si operacion=='a/b' Entonces
						resultado <- num_a/num_b;
						Escribir 'El resultado es ', resultado;
					SiNo
						Si operacion=='b/a' Entonces
							resultado <- num_b/num_a;
							Escribir 'El resultado es ', resultado;
						SiNo
							Escribir 'Operación no valida';
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
