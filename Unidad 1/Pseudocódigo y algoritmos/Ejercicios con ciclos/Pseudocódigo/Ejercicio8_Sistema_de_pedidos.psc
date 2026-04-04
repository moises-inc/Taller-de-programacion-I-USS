Proceso Ejercicio8_Sistema_de_pedidos
	
	// Ejercicio 8: Sistema de pedidos
	// Se ingresan pedidos de clientes hasta finalizar. Cada pedido puede ser normal o urgente. 
	// Contabilizar ambos tipos.
	
	Definir cantidad_pedidios, pedidios_normales, pedidios_urgentes, i Como Entero;
	Definir nivel_pedidio Como Caracter;
	
	pedidios_normales <- 0;
	pedidios_urgentes <- 0;
	
	Escribir "--- Sistema de pedidos ---";
	
	Escribir "Ingrese cantidad de pedidios: ";
	Leer cantidad_pedidios;
	
	Para i <- 1 Hasta cantidad_pedidios Con Paso 1 Hacer
		
		Escribir "Ingrese si el pedidio, ", i, " es urgente o normal";
		Leer nivel_pedidio;
		
		Si nivel_pedidio == "urgente" O nivel_pedidio = "Urgente" Entonces
			
			pedidios_urgentes <- pedidios_urgentes + 1;
		SiNo
			Si nivel_pedidio == "normal" O nivel_pedidio == "Normal" Entonces
				pedidios_normales <- pedidios_normales + 1;
			FinSi
		FinSi
		
	FinPara
	
	Escribir "La cantidad de pedidios urgentes es: ", pedidios_urgentes;
	Escribir "La cantidad de pedidios normales es: ", pedidios_normales;
	
FinProceso
