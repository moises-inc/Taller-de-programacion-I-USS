Proceso Ejercicio_2_5
	Definir peso_kg, estatura_m, Imc Como Real;
	Escribir 'Ingresa tu peso en kg (ejemplo: 83)';
	Leer peso_kg;
	Escribir 'Ingresa tu estatura en metros (ejemplo: 1.83)';
	Leer estatura_m;
	Imc <- peso_kg/(estatura_m)^2;
	Si Imc>=18.5 Y Imc<=24.9 Entonces
		Escribir 'Tu peso es normal y tu Imc es ', Imc;
	SiNo
		Si Imc>=25 Entonces
			Escribir 'Tienes sobrepeso y tu Imc es ', Imc;
		SiNo
			Escribir 'Tu peso esta bajo y tu Imc es ', Imc;
		FinSi
	FinSi
FinProceso
