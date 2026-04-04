Proceso Ejercicio9_Consumo_de_combustible
	// Ejercicio 9: Consumo de combustible
	// Un conductor registra litros cargados hasta ingresar 0. Mostrar total cargado y advertir si
	// supera los 50 litros.
	Definir litros_cargados, total_cargado Como Real;
	Definir validador Como Logico;
	total_cargado <- 0;
	validador <- Falso;
	Escribir '--- Consumo de combustible ---';
	Mientras validador==Falso Hacer
		Escribir 'Ingrese litros cargados o ingrese 0 para finalizar';
		Leer litros_cargados;
		Si litros_cargados==0 Entonces
			validador <- Verdadero;
		FinSi
		total_cargado <- total_cargado+litros_cargados;
		Si total_cargado>=50 Entonces
			Escribir 'Advertencia, esta superando los 50 litros';
		FinSi
	FinMientras
	Escribir 'El total cargado fue: ', total_cargado;
FinProceso
