Proceso Ejercicio_2_10
	Definir num_1, num_2 Como Real;
	Escribir 'Ingresa un número para ver si es multiplo del segundo número';
	Leer num_1;
	Escribir 'Ingresa un segundo número';
	Leer num_2;
	Si num_2 MOD num_1==0 Entonces
		Escribir 'El número ', num_1, ' es multiplo de ', num_2;
	SiNo
		Escribir 'El número ', num_1, ' no es multiplo de ', num_2;
	FinSi
FinProceso
