Proceso Ejercicio2_pre_solemne
	// Que permita calcular el promedio ponderado de 4 notas de cada estudiante para un curso
	// de n estudiantes, previo a iniciar el ingreso de notas, se debe ingresar la cantidad de
	// estudiantes y la ponderación para cada nota. El usuario debe proporcionar las notas de
		// cada estudiante. A cada estudiante se le debe ir mostrando su promedio y si aprobó o
			// no(aprueba >= 4), además considere calcular el promedio de todo el curso y mostrar una
			// vez se haya ingresado el último estudiante. Debe entregar el Pseudo código resultante y el
			// diagrama de flujo correspondiente, Recuerde que
	// Promedio ponderado = N1*(%pond1)+N2*(%pond2)+N3*(%pond3)+N4*(%pond4)
	
	Definir promedio_ponderado, estudiantes, notas, suma_notas, estudiantes_aprobados, estuantes_reprobados, promedio_general, i, nota_1, nota_2, nota_3,nota_4, nota_p1, nota_p2, nota_p3,nota_p4 Como Real;
	
	
	suma_notas<-0;
	
	Escribir "Ingrese cantidad de estudiantes: ";
	Leer estudiantes;
	
	Escribir "Ingrese ponderación de nota 1: ";
	Leer nota_p1;
	Escribir "Ingrese ponderación de nota 2: ";
	Leer nota_p2;
	Escribir "Ingrese ponderación de nota 3: ";
	Leer nota_p3;
	Escribir "Ingrese ponderación de nota 4: ";
	Leer nota_p4;
	
	Para i <- 1 Hasta estudiantes Con Paso 1 Hacer
		Escribir "Ingrese nota 1: ";
		Leer nota_1;
		Escribir "Ingrese nota 2: ";
		Leer nota_2;
		Escribir "Ingrese nota 3: ";
		Leer nota_3;
		Escribir "Ingrese nota 4: ";
		Leer nota_4;
		
		suma_notas<- suma_notas + nota_1+nota_3+nota_2+nota_4;
		
		promedio_ponderado <- (nota_1*nota_p1) + (nota_2*nota_p2)+(nota_3*nota_p3)+(nota_4*nota_p4);
		
		Si promedio_ponderado >= 4 Entonces
			Escribir "Usted aprobó";
		SiNo
			Escribir "Usted reprobó";
		FinSi
		
		Si i == estudiantes Entonces
			Escribir "Usted fué el último estudiante";
		FinSi
	FinPara
	
	promedio_general <- suma_notas/estudiantes; 
	
	Escribir "El promedio general es: ", promedio_general;

FinAlgoritmo

