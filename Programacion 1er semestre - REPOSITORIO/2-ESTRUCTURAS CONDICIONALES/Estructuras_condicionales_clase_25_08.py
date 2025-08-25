#DATOS
#Un instituto de inglés necesita un programa que le permita, 
# cada día, procesar observaciones sobre las clases de ese día. 
# El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: 
# los lunes se dicta nivel inicial, 
# los martes el nivel intermedio, 
# los miércoles el nivel avanzado, 
# los jueves son para práctica hablada 
# y los viernes se dicta inglés para viajeros.

#PRIMERA PARTE
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,DD/MM”, 
# donde [día] es un día de la semana (escrito en letras), DD es el número de día y MM es el número de mes. 
# Si el usuario ingresa un día de la semana inexistente 
# o una fecha cuyo día supere el número 31 
# o el mes supere el número 12, 
# finalizar el programa indicando que se produjo un error. 
# Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. 
# Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

#RESOLUCION 1RA PARTE
#Pedir la fecha actual al usuario
fecha_actual = input("Ingrese la fecha actual con el siguiente formato: día,DD/MM")

#Separar el dia (string), de la parte numerica (dia como numero, mes como numero)
# .split(".") Metodo de CADENAS DE TEXTO, que sirve para cortar un STRING usando un separador
#separador: puede ser un punto o una coma
parte_dia, parte_fecha = fecha_actual.split(",")


#Limpiar espacios
#quita los espacios de sobra AL PPIO y AL FINAL 
dia = parte_dia.strip()
fecha = parte_fecha.strip()

#Separar dia (DD) y mes(MM), ambos en numeros
dd_str, mm_str = fecha.split("/")      #la barra entre comillas!!!

#Convertir a numeros
dd = int(dd_str)
mm = int(mm_str)

#HACER UNA PRUEBA ANTES DE SEGUIR 
print(f"Dia ingresado: {dia}")
print(f"Dia numerico: {dd}")
print(f"Mes numerico: {mm}")

#AHORA HACER LAS VALIDACIONES

#VALIDAR EL DIA 
#DATO TIPO LIST, trabajo con las variables dia y dias_validos
dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes"]
if dia.lower() not in dias_validos:            #no te olvides de los dos puntos!!!!
    print("ERROR: LA PALABRA INGRESADA NO CORRESPONDE A UN DIA DE LA SEMANA")
    exit()

#VALIDAR EL DIA NUMERICO 
if dd < 1 or dd > 31:                          #los dos puntos florenciaaaaa!!!!!!!!
    print("ERROR: EL DIA INGRESADO NO CORRESPONDE A UN MES DEL AÑO.")
    exit()

#VALIDAR EL MES NUMERICO
if mm < 1 or mm > 12:                          #LOS DOS PUNTOS 
    print("ERROR: EL MES INGRESADO NO CORRESPONDE A UN MES DEL AÑO.")
    exit()

#AHORA SI PUEDO IMPRIMIR EL MENSAJE
#ANTES SOLO LA HABIA INGRESADO, PERO ANTES DE IMPRIMIRLA TENIA QUE HACER LAS VALIDACIONES
# Y PARA HACER LAS VALIDACIONES TENIA QUE TRABAJAR CON CADA DATO POR SEPARADO
print(f"La fecha ingresada es valida")


#SEGUNDA PARTE
#Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los exámenes,
# pero eso solo si se trata de los niveles inicial, intermedio o avanzado, 
# ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. 
# Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, 
# y el programa le mostrará el porcentaje de aprobados.

tomaron = input("¿Se tomaron exámenes? (s/n): ").lower()

if tomaron == "s":
    aprobados = int(input("Cantidad de alumnos aprobados: "))
    desaprobados = int(input("Cantidad de alumnos desaprobados: "))
    total = aprobados + desaprobados
    if total > 0:
        porcentaje = aprobados * 100 / total
        print(f"Porcentaje de aprobados: {porcentaje}%")
    else:
        print("No hay alumnos para calcular porcentaje.")
elif tomaron == "n":
    print("No se tomaron exámenes")
else:
    print("Respuesta inválida, por favor ingrese 's' o 'n'")

#Si el día fue el correspondiente a práctica hablada, 
# el usuario deberá ingresar el porcentaje de asistencia a clase 
# y el programa le indicará ‘asistió la mayoría’ 
# en caso de que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.

if dia.lower() == "jueves":                                #LOS DOS PUNTOOOOOOOOOOOOOOOOS
    presentes = int(input("Ingrese la cantidad de alumnos presentes: "))
    ausentes = int(input("Ingrese la cantidad de alumnos ausentes: "))
    total = presentes + ausentes 
    porcentajes = presentes * 100 / total
    
    if porcentajes > 50:
        print("Asistió la mayoría")
    else:
      print("No asistió la mayoría")

#Si se trata del inglés para viajeros 
# y la fecha actual corresponde al día 1 del mes 1 o del mes 7,
# se deberá imprimir ‘Comienzo de nuevo ciclo’ y 
# solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo 
# y el arancel en $ por cada alumno, 
# para luego imprimir el ingreso total en $.

if dia.lower() == "viernes" and dd == 1 and (mm == 1 or mm == 7):
    print("Comienzo de nuevo ciclo")
    alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    arancel = float(input("Ingrese el arancel por alumno en $: "))
    ingreso_total = alumnos * arancel
    print(f"Ingreso total: ${ingreso_total}")