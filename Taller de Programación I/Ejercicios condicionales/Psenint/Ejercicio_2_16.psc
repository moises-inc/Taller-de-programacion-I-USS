Proceso Ejercicio_2_16
	Definir color1, color2 Como Cadena;
	Escribir 'Ingresa un color primo (rojo, amarillo o azul): ';
	Leer color1;
	Escribir 'Ingresa un segundo color primo para conbinar: ';
	Leer color2;
	Si color1==color2 Entonces
		Escribir 'No hay mezcla, es el mismo color';
	SiNo
		Si ((color1=='rojo') Y (color2=='amarillo')) O ((color2=='rojo') Y (color1=='amarillo')) Entonces
			Escribir 'La mezcla es naranja';
		SiNo
			Si ((color1=='rojo') Y (color2=='azul')) O ((color2=='rojo') Y (color1=='azul')) Entonces
				Escribir 'La mezcla es morada';
			SiNo
				Si ((color1=='amarillo') Y (color2=='azul')) O ((color2=='amarillo') Y (color1=='azul')) Entonces
					Escribir 'La mezcla es verde';
				SiNo
					Escribir 'Combinación no reconocida';
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
