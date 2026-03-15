Proceso Ejercicio_2_0
	Definir numero_1 Como Real;
	Definir numero_2 Como Real;
	Escribir 'Ingrese nmero 1: ';
	Leer numero_1;
	Escribir 'Ingrese nmero 2: ';
	Leer numero_2;
	Si numero_1==numero_2 Entonces
		Escribir 'Los numeros son iguales';
	SiNo
		Si numero_1<numero_2 Entonces
			Escribir 'El número 2 es mayor';
		SiNo
			Escribir 'El numero 1 es mayor';
		FinSi
	FinSi
FinProceso
