Proceso Ejercicio7_Control_de_temperatura
	// Ejercicio 7: Control de temperatura
	// Una máquina reporta su temperatura constantemente. Si supera los 80 grados, se debe
	// emitir una alerta. Termina cuando la temperatura es -1
	Definir temperatura Como Real;
	temperatura <- 0;
	Escribir '--- Control de temperatura ---';
	Mientras temperatura<>-1 Hacer
		Escribir 'Ingrese temperatura registrada o ingrese -1 para detener el programa: ';
		Leer temperatura;
		Si temperatura>=80 Entonces
			Escribir 'Advertencia, la temperatura de la máquina esta superando los 80°';
		SiNo
			Si temperatura==-1 Entonces
				Escribir 'La temperatura registrada detendrá el programa';
			FinSi
		FinSi
	FinMientras
FinProceso
