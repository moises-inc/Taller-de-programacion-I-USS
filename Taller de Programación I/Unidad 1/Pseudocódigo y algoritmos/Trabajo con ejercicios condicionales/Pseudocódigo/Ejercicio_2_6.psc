Proceso Ejercicio_2_6
	Definir lado_1, lado_2, lado_3 Como Real;
	Escribir 'Ingresa medida de lado 1: ';
	Leer lado_1;
	Escribir 'Ingresa medida de lado 2: ';
	Leer lado_2;
	Escribir 'Ingresa medida de lado 3: ';
	Leer lado_3;
	Si lado_1==lado_2 Y lado_2==lado_3 Entonces
		Escribir 'Los lados son de un triángulo equilatero';
	SiNo
		Si (lado_1==lado_2) O (lado_1==lado_3) O (lado_2==lado_3) Entonces
			Escribir 'Los lados son de un triángulo isóceles';
		SiNo
			Escribir 'Los lados son de un triángulo escaleno';
		FinSi
	FinSi
FinProceso
