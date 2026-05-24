Proceso Ejercicio1
	
	// Ejercicio 1: Control de acceso a una plataforma
	// Una empresa tiene un sistema donde los usuarios deben ingresar su contraseña. El sistema 
	// permite hasta 3 intentos. Si falla los 3 intentos, se bloquea el acceso.
	
    Definir clave_correcta, clave_ingresada Como Caracter;
    Definir intentos Como Entero;
    Definir acceso_concedido Como Logico;
	
    clave_correcta <- "contraseña"; // Esta es la contraseña que el sistema espera (supuestamente)
    intentos <- 0;
    acceso_concedido <- Falso;   // Empezamos asumiendo que no tiene acceso
	
    Escribir "--- SISTEMA DE SEGURIDAD ---";
	
    // Bucle: Se repite MIENTRAS los intentos sean menores a 3 Y no tenga acceso
    Mientras (intentos < 3) Y (acceso_concedido == Falso) Hacer
        
        Escribir "Ingrese su contraseña: ";
        Leer clave_ingresada;
		
        // Evaluamos si acertó
        Si (clave_ingresada == clave_correcta) Entonces
            acceso_concedido <- Verdadero;// Se cambia el valor de verdad para que el bucle se detenga
        Sino
            intentos <- intentos + 1;
            Escribir "Contraseña incorrecta.";
            Escribir "Le quedan ", (3 - intentos), " intento(s).";
        Fin Si
		
    Fin Mientras
	
    // Conclusión fuera del bucle
    Si (acceso_concedido == Verdadero) Entonces
        Escribir "¡Acceso concedido! Bienvenido al sistema";
    Sino
        Escribir "SISTEMA BLOQUEADO: Ha superado el límite de 3 intentos.";
    Fin Si
	
	
	
FinProceso
