Proceso Ejercicio_4
	// Ejercicio 4: Cajero automático
	// Un usuario puede retirar dinero mientras tenga saldo disponible. Si intenta retirar más de lo
	// permitido, el sistema debe advertirlo.
	Definir dinero_disponible, dinero_retirado Como Real;
	Escribir '--- Cajero Automático ---';
	Escribir 'Ingrese saldo disponible inicial: ';
	Leer dinero_disponible;
	// Es más seguro usar > 0 en lugar de <> 0.
	// Al usar <> 0 (distinto de cero) y por algún error lógico el saldo llegara a ser -10,
	// el bucle seguiría ejecutándose infinitamente, porque -10 es distinto de cero.
	// Usar > 0 es un excelente mecanismo de seguridad.
	Mientras dinero_disponible>0 Hacer
		Escribir 'Saldo actual: $', dinero_disponible;
		Escribir 'Ingrese la cantidad que desee retirar: ';
		Leer dinero_retirado;
		// 1. Primero evaluamos si el retiro supera el saldo disponible
		Si dinero_retirado>dinero_disponible Entonces
			Escribir 'Advertencia: No tiene saldo suficiente para retirar esa cantidad. Inténtelo de nuevo.';
		SiNo
			// 2. Si el retiro es válido (menor o igual al saldo), ENTONCES restamos
			dinero_disponible <- dinero_disponible-dinero_retirado;
			// 3. Verificamos si la cuenta quedó en cero tras la resta válida
			Si dinero_disponible==0 Entonces
				Escribir 'Se acabó el saldo disponible. El programa se detendrá.';
			SiNo
				Escribir 'Retiro exitoso. Su nuevo saldo es: $', dinero_disponible;
			FinSi
		FinSi
	FinMientras
FinProceso
