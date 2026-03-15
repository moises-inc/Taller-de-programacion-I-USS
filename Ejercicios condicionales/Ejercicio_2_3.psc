Proceso Ejercicio_2_3
	Definir edad Como Entero;
	Escribir 'Ingresa tu edad';
	Leer edad;
	Si edad>=65 Entonces
		Escribir 'Eres tercera edad';
	SiNo
		Si edad>=18 Y edad<65 Entonces
			Escribir 'Eres mayor de edad';
		SiNo
			Escribir 'Eres menor de edad';
		FinSi
	FinSi
FinProceso
