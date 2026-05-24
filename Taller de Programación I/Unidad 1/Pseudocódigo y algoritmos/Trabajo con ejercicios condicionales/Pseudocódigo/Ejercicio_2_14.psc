Proceso Ejercicio_2_14
	Definir opcion Como Entero;
	Definir valor, resultado Como Real;
	Escribir 'Seleccione una conversión (1, 2 o 3): ';
	Escribir '1. Centimetros a pulgadas';
	Escribir '2. Kilogramos a libras';
	Escribir '3. Litros a galones';
	Leer opcion;
	Escribir 'Ingresa valor a convertir: ';
	Leer valor;
	Si opcion==1 Entonces
		resultado <- valor/2.54;
		Escribir valor, ' cm a pulgadas es ', resultado, ' pulgadas';
	SiNo
		Si opcion==2 Entonces
			resultado <- valor/0.45359237;
			Escribir valor, ' Kg a libras es ', resultado, ' libras';
		SiNo
			Si opcion==3 Entonces
				resultado <- valor/3.785411784;
				Escribir valor, ' litros a galones es ', resultado, ' galones';
			SiNo
				Escribir 'Opción no valida';
			FinSi
		FinSi
	FinSi
FinProceso
