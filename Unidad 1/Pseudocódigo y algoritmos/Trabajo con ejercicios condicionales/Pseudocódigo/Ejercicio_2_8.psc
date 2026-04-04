Proceso Ejercicio_2_8
	Definir anio Como Entero;
	Escribir 'Ingresa un año para saber si es bisiesto o no: ';
	Leer anio;
	Si ((anio MOD 4==0) Y ((anio MOD 100<>0) O (anio MOD 400==0))) Entonces
		Escribir 'El año ', anio, ' es bisiesto';
	SiNo
		Escribir 'El año no es bisiesto';
	FinSi
FinProceso
