Proceso Ejercicio_2_2
	Definir num_1, num_2, num_3 Como Real;
	Escribir 'Ingresa un número 1';
	Leer num_1;
	Escribir 'Ingresa un número 2';
	Leer num_2;
	Escribir 'Ingresa un número 3';
	Leer num_3;
	Si num_1>num_2 Y num_1>num_3 Entonces
		Escribir 'El número mayor es ', num_1;
	SiNo
		Si num_2>num_1 Y num_2>num_3 Entonces
			Escribir 'El número mayor es ', num_2;
		SiNo
			Escribir 'El número mayor es ', num_3;
		FinSi
	FinSi
FinProceso
