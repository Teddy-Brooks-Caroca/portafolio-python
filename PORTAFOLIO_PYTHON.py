### PORTAFOLIO PYTHON ###

## 1. Introducción, conceptos y condicionales

# Ejercicio 1: Crear un programa que pida al usuario su nombre y edad, luego muestre un mensaje personalizado indicando si es mayor o menor de edad.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print(f"{nombre.upper()} usted es menor de edad")
elif edad >= 18:
    print(f"{nombre.upper()} usted es mayor de edad")
else:
    print("Ingrese una edad permitida por el sistema")

# Ejercicio 2: Diseñar un programa que calcule el precio total de una compra, aplicando descuentos según el monto.

precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el descuento ofrecido: "))

descuento = (precio * porcentaje_descuento) / 100

precio_final = precio - descuento

print("==== DETALLE ====")
print(f"PRECIO ORIGINAL: ${precio:.2f}")
print(f"DESCUENTO: {porcentaje_descuento:.2f}%")
print(f"PRECIO FINAL: ${precio_final:.2f}")
print("==== === === ====")

# Ejercicio 3: Escribir un programa que convierta grados Celsius a Fahrenheit y viceversa, con una opción de menú para elegir la conversión.

print(":::::: Conversor de temperatura ::::::")

while True:
    print("\n1.- Convertir a grados Celsius",
          "\n2.- Convertir a grados Fahrenheit",
          "\n3.- Salir")

    opcion = input("Ingrese una de las opciones: ")

    if opcion == "1":
        grados = float(input("Ingrese la temperatura en Fahrenheit: "))
        conversion_f_x_c = (grados - 32) * 5 / 9
        print(f"{grados}°F son {conversion_f_x_c:.2f}°C")

    elif opcion == "2":
        grados = float(input("Ingrese la temperatura en Celsius: "))
        conversion_c_x_f = (grados * 1.8) + 32
        print(f"{grados}°C son {conversion_c_x_f:.2f}°F")

    elif opcion == "3":
        print(":::::: Gracias por usar el conversor ::::::")
        break

    else:
        print("Opción no válida, intente nuevamente.")

# Ejercicio 4: Crear un programa que determine si un número ingresado por el usuario es positivo, negativo o cero.

numero_usuario = int(input("Ingrese un numero: "))

if numero_usuario > 0:
    print("El número ingresado es positivo")
elif numero_usuario < 0:
    print("El número ingresado es es negativo")
else:
    print("El número ingresado es igual a 0")
    
# Ejercicio 5: Implementar un programa que identifique el mayor de tres números ingresados por el usuario.

num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
num3 = float(input("Ingrese tercer número: "))

mayor = max(num1, num2, num3)
print(f"El número mayor es: {mayor}")
    
# Ejercicio 6: Diseñar un menú interactivo que permita seleccionar opciones como "Sumar", "Restar" o "Salir".

print("::::: CALCULADORA SIMPLE :::::")
while True:

    print("1 - Sumar","\n"
          "2 - Restar","\n"
          "3 - Multiplicar","\n"
          "4 - Dividir","\n"
          "5 - Salir") 

    opcion = input("Escoga una de las opciones: ")

    if opcion == "1":
        print("::::::::::::::::::::::::::::::::::::")
        num_1 = int(input("Ingrese primer numero: "))
        num_2 = int(input("Ingrese segundo número:")) 
        suma = num_1 + num_2
        print(f"{num_1} + {num_2} = {suma}")
        print("::::::::::::::::::::::::::::::::::::")
    
    elif opcion == "2":
        print("::::::::::::::::::::::::::::::::::::")
        num_1 = int(input("Ingrese primer numero: "))
        num_2 = int(input("Ingrese segundo número:")) 
        resta = num_1 - num_2
        print(f"{num_1} - {num_2} = {resta}")
        print("::::::::::::::::::::::::::::::::::::")
    
    elif opcion == "3":
        print("::::::::::::::::::::::::::::::::::::")
        num_1 = int(input("Ingrese primer numero: "))
        num_2 = int(input("Ingrese segundo número:")) 
        mult = num_1 * num_2
        print(f"{num_1} x {num_2} = {mult}")
        print("::::::::::::::::::::::::::::::::::::")
    
    elif opcion == "4":
        print("::::::::::::::::::::::::::::::::::::")
        num_1 = int(input("Ingrese primer numero: "))
        num_2 = int(input("Ingrese segundo número:")) 
        divd = num_1 / num_2
        print(f"{num_1} / {num_2} = {divd}")
        print("::::::::::::::::::::::::::::::::::::")
    
    elif opcion == "5":
        print("::::::::::::::::::::::::::::::::::::")
        print("Ha salido de la calculadora")
        print("::::::::::::::::::::::::::::::::::::")
        break

    else:
        print("::::::::::::::::::::::::::::::::::::")
        print("Solo las opciones permitidas")    
        print("::::::::::::::::::::::::::::::::::::")


# Ejercicio 7: Simular un sistema de autenticación básico que valide un usuario y contraseña predefinidos.

nombre_usuario = input("Ingrese su nombre de usuario: ").strip().lower()
contraseña = input("Ingrese su contraseña: ")

if nombre_usuario == "johndoe" and contraseña == "071085":
    print("Usuario y contraseña válidos. Bienvenido.")
else:
    print("Usuario o contraseña incorrectos.")


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## 2. Entrada de datos, bucles y listas

# Ejercicio 1: Crear un programa que sume todos los números introducidos por el usuario hasta que se ingrese un "0".

print("::::: Secuencia con bucle infinito :::::")

lista_de_numeros = []

while True:
    nuevo_numero = int(input("Ingrese nuevo numero: "))
    if nuevo_numero == 0:
        print("::::::: La secuencia ha termiando ::::::")
        break
    lista_de_numeros.append(nuevo_numero)
    print(lista_de_numeros)
    print(f"Has ingresado {len(lista_de_numeros)} números")
    print(f"La suma de los numeros ingresados es: {sum(lista_de_numeros)}")
    print(":::::::::::::::::::::::::::::::::::::::")

# Ejercicio 2: Escribir un programa que genere una lista de números del 1 al 10 y los imprima en orden inverso.

lista_de_numeros = []

for n in range(1,11):
    lista_de_numeros.append(n)

print(lista_de_numeros[::-1]) # primer método

lista_de_numeros.reverse() # segundo método
print(lista_de_numeros)

# Ejercicio 3: Implementar un programa que calcule el promedio de una lista de números ingresados por el usuario.

print(":::: Operación matematica simple en bucle ::::")

lista_de_notas = []

contador = 0

cantidad_de_notas = int(input("Cuantas notas desea promediar: "))

while cantidad_de_notas > contador:
    nueva_nota = int(input("Ingrese nueva nota: "))
    lista_de_notas.append(nueva_nota)
    contador += 1

promedio = sum(lista_de_notas) / cantidad_de_notas

print(":::::::::::::::::::::::::::::::::::")
print(f"Sus notas son: {lista_de_notas}")
print(f"Su promedio es: {promedio}")
print(":::::::::::::::::::::::::::::::::::")

# Ejercicio 4: Crear un programa que lea un texto y cuente cuántas vocales contiene.

print(":::: Manipulación de cadenas de texto con bucle for ::::")

frase = input("Ingrese texto a analizar: ")

frase_cortada = frase.split()

contador_vocales = 0

for palabra in frase_cortada:
    for letra in palabra:
        if letra.lower() in "aeiou":
            contador_vocales += 1

print(f"Su frase tiene {contador_vocales} vocales")

# Ejercicio 5: Diseñar un sistema para ingresar y almacenar nombres en una lista, con opción de eliminar duplicados.

print(":::: MANIPULACION DE LISTAS EN BUCLES ::::")

lista_de_nombre = []

lista_sin_duplicados = []

while True:

    nuevo_nombre = input("Ingrese nuevo nombre o escriba 'salir': ")

    if nuevo_nombre.lower() == "salir":
        print("Ha salido del programa")
        print(":::::::::::::::::::::::::::::::::::::::::::::")
        break
    else:
        lista_de_nombre.append(nuevo_nombre)

for nombre in lista_de_nombre:
     if nombre not in lista_sin_duplicados:
         lista_sin_duplicados.append(nombre)

print(f"Lista original: {lista_de_nombre}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
print(":::::::::::::::::::::::::::::::::::::::::::::")

eliminar_duplicados = input("Desea eliminar duplicados (si/no): ")

if eliminar_duplicados.lower() == "si":
    lista_sin_duplicados = []
    for nombre in lista_de_nombre:
        if nombre not in lista_sin_duplicados:
            lista_sin_duplicados.append(nombre)
    
    print(f"Lista corregida:{lista_sin_duplicados}")
    print(":::::::::::::::::::::::::::::::::::::::::::::")

else:
    print("Se mantienen ambas listas")
    print(":::::::::::::::::::::::::::::::::::::::::::::")

if eliminar_duplicados.lower() == "si":                    #OTRA MANERA ES USANDO EL METODO .copy()
    lista_de_nombre = lista_sin_duplicados.copy()
    print(f"Lista actualizada: {lista_de_nombre}")
    print(":::::::::::::::::::::::::::::::::::::::::::::")
else:
    print("Se mantienen ambas listas")
    print(":::::::::::::::::::::::::::::::::::::::::::::")


#Ejercicio 6: Generar una tabla de multiplicar usando bucles anidados.

multiplicando = int(input("Ingrese el número para la tabla de multiplicar: "))

for _ in range(1):  
    for multiplicador in range(1, 11):  
        print(f"{multiplicando} x {multiplicador} = {multiplicando * multiplicador}")


multiplicando = int(input("Ingrese la tabla que desea: "))            # MÉTODO TRADICIONAL, SIN ANIDADO
multiplicador = int(input("Ingrese hasta que numero desea la tabla: "))

for n in range(1,multiplicador + 1):
    print(f"{multiplicando} x {n} = {multiplicando * n}")

# Ejercicio 7: Construir un programa que simule un cajero automático con saldo inicial, depósitos y retiros.

print("::::: SIMULACIÓN DE CAJERO AUTOMÁTICO :::::")
print("manipulación de bucles y condicionales en lista")
print(":::::::::::::::::::::::::::::::::::::::::::")

depositos = []
retiros = []

clave = input("Ingrese su clave: ")

if clave == "0710":

    while True:

        saldo = sum(depositos) - sum(retiros)

        print("1.- Consultar saldo","\n"
              "2.- Depositar","\n"
              "3.- Retirar","\n"
              "4.- Salir")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print(f"Su saldo actual es de: ${saldo}")

        elif opcion == "2":
            deposito = float(input("Ingrese la cantidad que desea depositar: "))
            confirmacion_deposito = input(f"Usted quiere depositar ${deposito} ¿Es correcta la cifra? (si/no): ")
            if confirmacion_deposito.lower() == "si":
                depositos.append(deposito)
                print("Su deposito ha sido registrado con éxito")
                print("::::::::::::::::::::::::::::::::::::::::")

            else:
                deposito_corregido = float(input("Ingrese nuevamente la cantidad que desea depositar: "))
                depositos.append(deposito_corregido)
                print("Su deposito ha sido registrado con éxito")
                print("::::::::::::::::::::::::::::::::::::::::")

        elif opcion == "3":
            retiro = float(input("Ingrese la cantidad que desea retirar: "))
            confirmacion_retiro = input(f"Usted quiere retirar ${retiro} ¿Es correcta la cifra? (si/no): ")
            if confirmacion_retiro.lower() == "si":
                if retiro < saldo:
                    retiros.append(retiro)
                    print("Su retiro ha sido registrado con éxito")
                    print("::::::::::::::::::::::::::::::::::::::::")

                else:
                    print("Su saldo es menor a lo que desea retirar")
                    print("::::::::::::::::::::::::::::::::::::::::")

            else:
                retiro_corregido = float(input("Ingrese nuevamente la cantidad que desea retirar: "))
                if retiro_corregido < saldo:
                    retiros.append(retiro_corregido)
                    print("Su retiro ha sido registrado con éxito")
                    print("::::::::::::::::::::::::::::::::::::::::")

        elif opcion == "4":
            print("Usted ha salido del programa")
            print("::::::::::::::::::::::::::::::::::::::::")
            break

else:
    print("Clave ingresada no es la correcta")
    print("::::::::::::::::::::::::::::::::::::::::")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## 3. Colecciones, diccionarios y funciones

# Ejercicio 1: Crear una función que reciba una lista y devuelva el elemento más grande y el más pequeño.

print(" :::: CREACIÓN DE FUNCIÓN SIN DEPENDECIA DE VARIABLES GLOBALES :::: ")

lista_de_numeros = []

cantidad_de_elementos = int(input("Cuentos números desea ingresar: "))
contador_de_elementos = 0

while cantidad_de_elementos > contador_de_elementos:
    elemento = int(input("Ingrese número a la lista: "))
    lista_de_numeros.append(elemento)
    contador_de_elementos = contador_de_elementos + 1

def lista_maximo_minimo(lista):
    return min(lista), max(lista)

minimo, maximo = lista_maximo_minimo(lista_de_numeros)

print(":::::::::::::::::::::::::::::::::::")
print(f"El número más pequeño es: {minimo}")
print(f"El número más grande es: {maximo}")
print(":::::::::::::::::::::::::::::::::::")

# Ejercicio 2: Escribir un programa que use un diccionario para almacenar la relación entre nombres y edades, y permita buscar datos.

print(":::: MANEJO DE FUNCIONES EN BUCLES Y DICCIONARIOS ::::")

datos_personales = {}

def mostrar_lista(personas):
    print("::::::::::::::::::::::::::::::::::::::::")
    print("PERSONAS INGRESADAS:")
    contador = 1
    for nombre,edad in personas.items():
        print(f"{contador}.- {nombre.upper()} tiene {edad} años")
        contador = contador + 1


while True:
    
    nombre = input("Ingrese nombre completo de la persona o escriba 'salir': ")

    if nombre.lower() == "salir":
        mostrar_lista(datos_personales)
        print("Usted ha salido del programa")
        print("::::::::::::::::::::::::::::::::::::::::")
        break

    else:
        edad = int(input("Escriba la edad de la persona: "))
        print("::::::::::::::::::::::::::::::::::::::::")
        datos_personales[nombre] = edad

revisar_nombre = input("Ingrese nombre de la persona: ")

if revisar_nombre in datos_personales:
    print(f"{revisar_nombre.upper()} tiene {datos_personales[revisar_nombre]} años")
    print("::::::::::::::::::::::::::::::::::::::::")

else:
     print("Nombre no ha sido encontrado")
     print("::::::::::::::::::::::::::::::::::::::::")

# Ejercicio 3: Implementar una función que calcule la suma de los valores en un diccionario.

print(" :::: DICCIONARIOS EN BUCLES CON FUNCIONES :::: ")

diccionario_numeros = {}

def sumar_diccionario():
    return sum(diccionario_numeros.values())

def mostrar_conjuntos(diccionario):
    print(":: Conjuntos ingresados ::")
    for clave,valor in diccionario.items():
        print(f"{clave}: {valor}")

while True:

    clave = input("Ingrese 'conjunto' seguido de una letra, sino escriba 'salir': ")

    if clave.lower() == "salir":
        mostrar_conjuntos(diccionario_numeros)
        print(":" * 50)
        break

    if clave in diccionario_numeros:
        print(f"La clave{clave} ya existe. Ingrese una nueva clave")
        continue

    else:
        valor = int(input("Ingrese el valor que desea: "))
        print(":" * 50)
        diccionario_numeros[clave] = valor

resultado = sumar_diccionario()
print(f"Su resultado es: {resultado}")
print(":" * 50)

# Ejercicio 4: Diseñar una función que reciba una tupla de números y devuelva su promedio.

print(" :::: FUNCIONES EN TUPLAS ::::")

numeros_en_lista = []

def promedio(numero):
    if len(numero) == 0:
        return "No se puede calcular el promedio con una lista vacía"
    return sum(numero) / len(numero)


contador = 0

while True:
    try:
        cantidad_de_numeros = int(input("¿Cuántos números desea agregar?: "))
        if cantidad_de_numeros <= 0:
            print("Debe ingresar un número mayor a cero.")
            print(":"* 40)
            continue
        break 
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        print(":"* 40)
              
while contador < cantidad_de_numeros:
    numero_a_ingresar = int(input("Ingrese un numero: "))
    numeros_en_lista.append(numero_a_ingresar)
    contador = contador + 1

numeros_en_tupla = tuple(numeros_en_lista)

print(f"Su promedio es: {promedio(numeros_en_tupla)}")
print(":"* 40)

#Ejercicio 5: Crear un programa que almacene notas de estudiantes en un diccionario y calcule el promedio de cada uno.

print(":::: FUNCIONES EN DICCIONARIO ::::")
print(":: simulación de promedio en diccionario ::")

notas_estudiantes = {}

def promedio_estudiante(numero):
    return sum(numero) / len(numero)

def lista_estudiantes(diccionario):
    print("::: Alumnos ingresados :::")
    for estudiante,nota in diccionario.items():
        print(f"{estudiante.upper()}:{nota}")


while True:

    estudiante = input("Ingrese nombre y apellido del estudiante o 'salir': ")

    if estudiante.lower() == 'salir':
        lista_estudiantes(notas_estudiantes)
        print(":" * 50)
        break

    else:
        try:
            nota = float(input("Ingrese calificación del estudiante: "))
        except ValueError:
            print("Debe ingresar nota con decimal")
            continue

        if estudiante not in notas_estudiantes:
            notas_estudiantes[estudiante] = []
            notas_estudiantes[estudiante].append(nota)
                
        while True:

            confirmacion = input("Desea agregar otra calificación(si/no): ")
            print(":" * 50)

            if confirmacion == "si": 
                try:
                    nueva_nota = float(input("Ingrese nueva nota: "))
                    print(":" * 50)
                except ValueError:
                    print("Ingresar nota con decimal")
                    continue

                notas_estudiantes[estudiante].append(nueva_nota)

            else:
                print("Notas del estudiante completado")
                print(":" * 50)
                break

estudiante_promedio = input("Ingrese nombre completo del estudiante o escriba 'salir': ")
print(":" * 50)

if estudiante_promedio in notas_estudiantes:
    resultado = promedio_estudiante(notas_estudiantes[estudiante_promedio])
    print(f"El promedio de {estudiante_promedio.upper()} es: {resultado}")
    print(":" * 50)

else:
    print("Usted ha salido del programa")
    print(":" * 50)

# Ejercicio 6: Implementar un programa que permita registrar tareas pendientes en un diccionario con categorías.

print(" :::: MANIPULACIÓN DE DICCIONARIO :::: ")

tareas_pendientes = {}
    
while True:

    turno = input("Escriba 'mañana','tarde','noche' o 'salir': ").lower().strip()

    if turno.isdigit():
            print("No se permite poner números en el turno")
            print(":" * 50)
            continue

    if turno == "salir":
        for turno, tareas in tareas_pendientes.items():
            print(f"Turno {turno.capitalize()}:")
            for tarea in tareas:
                print(f"  - {tarea}")
        print(":" * 50)
        break
    
    
    tarea = input("Ingrese la tarea que debe de realizar: ")
    
    if tarea.isdigit():
        print("No se permite poner números en el turno")
        print(":" * 50)
        continue
        
    tareas_pendientes.setdefault(turno, []).append(tarea) # Con este método agregamos valores en repetidas oportunidades 

        
    while True:

        confirmacion = input("Desea agregar otra tarea (si/no): ").strip().lower()
        print(":" * 50)
        

        if confirmacion == "si":
            nueva_tarea = input("Ingrese nueva tarea: ").strip()

            if nueva_tarea.isdigit():
                print("Error: No se permiten números en la tarea.")
                continue

            tareas_pendientes[turno].append(nueva_tarea)
        
        elif confirmacion == "no":
            print("Lista de tareas completadas")
            print(":" * 50)
            break
        
        else:
            print("Solo se permite poner si o no")
            print(":" * 50)
            

lista_turno = input("Ingrese turno que desea ver las tareas: ")

if lista_turno in tareas_pendientes:
    print(f"Para el turno de {lista_turno} usted tiene pendiente: ")
    for tarea in tareas_pendientes[lista_turno]:
        print(tarea)
    print(":" * 50)

# Ejercicio 7: Crear un generador de contraseñas aleatorias utilizando colecciones.

import random as rm
import string as st

letras = st.ascii_letters
digitos = st.digits
especiales = st.punctuation

alfabeto = letras + digitos + especiales 

longitud_contraseña = 15

contraseña = ""

for caracter in range(longitud_contraseña):
    contraseña += rm.choice(alfabeto)

print(f"Su contraseña es: {contraseña}")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## 4. Bibliotecas y aplicaciones de escritorio

# Ejercicio 1: Crear un script que use la biblioteca math para resolver ecuaciones cuadráticas.

print("::::: ECUACIONES CUADRÁTICAS CON BIBLIOTECA :::::")

import math as mt
import cmath as cmat

a = int(input("Ingrese valor para valor 'a': "))
b = int(input("Ingrese valor para valor 'b': "))
c = int(input("Ingrese valor para valor 'c': "))

exponente = 2

discriminante = pow(b,exponente) - (4*a*c)

if discriminante > 0:
    x1 = (-b + mt.sqrt(discriminante))/(2*a)
    x2 = (-b - mt.sqrt(discriminante))/(2*a)
    print(f"::: FORMULA CUADRÁTICA :::")
    print(f"-{b} ± √( {b}² - 4* {a} * {c} ) / 2 * {a}")
    print(f"Las soluciones reales son: {x1} y {x2}")
    print(":"*50)

elif discriminante < 0:
    x3 = (-b + cmat.sqrt(discriminante))/(2*a)
    x4 = (-b - cmat.sqrt(discriminante))/(2*a)
    print(f"::: FORMULA CUADRÁTICA :::")
    print(f"-{b} ± √( {b}² - 4 * {a} * {c} ) / 2 * {a}")
    print(f"Las soluciones complejas son: {x3} y {x4}")
    print(":"*50)

else:
    x = -b / (2*a)
    print(f"::: FORMULA CUADRÁTICA :::")
    print(f"-{b} / 2 * {a}")
    print(f"La única solución real es: {x}")
    print(":"*50)

# Ejercicio 2: Diseñar un programa que utilice random para simular el lanzamiento de un dado.

print(" :::: USO DE BIBLIOTECAS :::: ")
print(" ::: simulación de dado ::: ")

import random as rm
import time as tm

while True:

    tirar_dado = input("Presiona '7' para tirar dado o escribe 'salir': ").lower()

    if tirar_dado == "salir":
        print("Usted no quiso lanzar el dado")
        print(":" * 50)
        break

    elif tirar_dado == "7":
        dado_lanzado = rm.randint(1,6)
        tm.sleep(3)
        print(f"El dado cayó en: {dado_lanzado}")
        print(":" * 50)
    
    else:
        print("Solo debe escribir '7' o 'salir'")
        print(":" * 50)


# Ejercicio 3: Escribir un programa que genere un gráfico de barras con datos ficticios usando matplotlib.

print(":::::: MANEJO DE LIBRERIAS ::::::")
print(":: simulación ingreso y graficación ::")

import matplotlib.pyplot as plt

comunidades_indigenas = {}

while True:
    nombre_comunidad = input("Ingrese el nombre de la comunidad o escriba 'salir': ").lower()
    print(":" * 50)

    if nombre_comunidad == "salir":
        print("Usted ha salido del programa")
        print(":" * 50)
        break

    else:
        try:
            cantidad_habitantes = int(input("Ingrese la cantidad de habitantes registrada: "))
        except ValueError:
            print("Debe escribir sin decimales")
            continue
        
        comunidades_indigenas[nombre_comunidad] = cantidad_habitantes
        print(":" * 50)

comunidad = list(comunidades_indigenas.keys())

cantidad = list(comunidades_indigenas.values())


plt.bar(comunidad,cantidad)
plt.title("Distribución de habitantes por comunidad indígena")
plt.xlabel("Comunidades indígenas")
plt.ylabel("Cantidad de habitantes")
plt.xticks(rotation=45)

plt.show()

# Ejercicio 4: Implementar un programa que use tkinter para crear una interfaz que permita sumar dos números.

import tkinter as tk

def sumar():
    try:
        valor1 = caja_primer_numero.get()
        valor2 = caja_segundo_numero.get()
        numero1 = float(valor1)
        numero2 = float(valor2)
        resultado = numero1 + numero2
        caja_resultado.config(state="normal")
        caja_resultado.delete(0, tk.END)
        caja_resultado.insert(0, resultado)
        caja_resultado.config(state="readonly")

    except ValueError:
         caja_resultado.config(state="normal")
         caja_resultado.delete(0, tk.END)
         caja_resultado.insert(0, "Error")
         caja_resultado.config(state="readonly")
        

# CREAMOS LA VENTANA
ventana = tk.Tk()
ventana.config(width= 300,height=250)
ventana.title(":::: Sumatoria simple ::::")

# CONFIGURAMOS LA PRIMERA ENTRADA
etiqueta_primer_numero = tk.Label(text="Ingrese primer numero:")
etiqueta_primer_numero.place(x=30,y=30)
caja_primer_numero = tk.Entry()
caja_primer_numero.place(x=170, y=30,width=80,height=20)

# CONFIGURAMOS LA SEGUNDA ENTRADA
etiqueta_segundo_numero = tk.Label(text="Ingrese segundo numero:")
etiqueta_segundo_numero.place(x=30,y=60)
caja_segundo_numero = tk.Entry()
caja_segundo_numero.place(x=170, y=60,width=80,height=20)

# CONFIGURAMOS LA TERCERA ENTRADA
etiqueta_resultado = tk.Label(text="Su resultado:")
etiqueta_resultado.place(x=30,y=90)
caja_resultado = tk.Entry()
caja_resultado.place(x=170, y=90,width=120,height=20)

# CONFECCIONAMOS LA BOTONERA
boton_resultado = tk.Button(text = "SUMAR",command= sumar) # en la función convertimos a INT o FLOAT
boton_resultado.place(x = 30, y = 120)

# VISUALIZAMOS EL LA VENTANA
ventana.mainloop()

# Ejercicio 5: Crear una pequeña calculadora gráfica con operaciones básicas usando tkinter.

import tkinter as tk

# Inicialización de variables globales
primer_numero = 0
operador = ""

def agregar_numero(num):
    caja_botones.config(state="normal")
    caja_botones.insert(tk.END, str(num))
    caja_botones.config(state="readonly")

def agregar_punto():                    # Verifica si ya hay un punto decimal en la caja
    if "." not in caja_botones.get():
        caja_botones.config(state="normal")
        caja_botones.insert(tk.END, ".")
        caja_botones.config(state="readonly")

def operacion(simb):
    global primer_numero, operador
    primer_numero = float(caja_botones.get())
    operador = simb
    caja_botones.config(state="normal")
    caja_botones.delete(0, tk.END) 
    caja_botones.config(state="readonly")

def calcular():
    global primer_numero, operador
    segundo_numero = float(caja_botones.get())  # Obtiene el segundo número
    caja_botones.config(state="normal")
    caja_botones.delete(0, tk.END)

    if operador == "+":
        resultado = primer_numero + segundo_numero
    elif operador == "-":
        resultado = primer_numero - segundo_numero
    elif operador == "*":
        resultado = primer_numero * segundo_numero
    elif operador == "/":
        resultado = primer_numero / segundo_numero if segundo_numero != 0 else "Error"

    caja_botones.insert(0, resultado)
    caja_botones.config(state="readonly")

def limpiar():
    global primer_numero, operador
    primer_numero = 0
    operador = ""
    caja_botones.config(state="normal")
    caja_botones.delete(0, tk.END)
    caja_botones.config(state="readonly")

# CREAMOS LA VENTANA
ventana_calculadora = tk.Tk()
ventana_calculadora.config(width=200, height=300)
ventana_calculadora.title("Calculadora")

# CONFIGURAMOS LA CAJA
caja_botones = tk.Entry()
caja_botones.place(x=30, y=30, width=120, height=20)
caja_botones.config(state="readonly")  # Inicializar como readonly

# CREAMOS LOS BOTONES
boton_0 = tk.Button(text="0", command=lambda: agregar_numero(0))
boton_0.place(x=30, y=150)

boton_1 = tk.Button(text="1", command=lambda: agregar_numero(1))
boton_1.place(x=30, y=60)

boton_2 = tk.Button(text="2", command=lambda: agregar_numero(2))
boton_2.place(x=60, y=60)

boton_3 = tk.Button(text="3", command=lambda: agregar_numero(3))
boton_3.place(x=90, y=60)

boton_4 = tk.Button(text="4", command=lambda: agregar_numero(4))
boton_4.place(x=30, y=90)

boton_5 = tk.Button(text="5", command=lambda: agregar_numero(5))
boton_5.place(x=60, y=90)

boton_6 = tk.Button(text="6", command=lambda: agregar_numero(6))
boton_6.place(x=90, y=90)

boton_7 = tk.Button(text="7", command=lambda: agregar_numero(7))
boton_7.place(x=30, y=120)

boton_8 = tk.Button(text="8", command=lambda: agregar_numero(8))
boton_8.place(x=60, y=120)

boton_9 = tk.Button(text="9", command=lambda: agregar_numero(9))
boton_9.place(x=90, y=120)

boton_punto = tk.Button(text=".", command=agregar_punto)
boton_punto.place(x=120, y=150)

boton_suma = tk.Button(text="+", command=lambda: operacion("+"))
boton_suma.place(x=60, y=150)

boton_resta = tk.Button(text="-", command=lambda: operacion("-"))
boton_resta.place(x=90, y=150)

boton_mult = tk.Button(text="*", command=lambda: operacion("*"))
boton_mult.place(x=30, y=180)

boton_div = tk.Button(text="/", command=lambda: operacion("/"))
boton_div.place(x=60, y=180)

boton_igual = tk.Button(text="=", command=calcular)
boton_igual.place(x=90, y=180)

boton_limpiar = tk.Button(text="C", command=limpiar)
boton_limpiar.place(x=120, y=180)

# VISUALIZAMOS LA VENTANA
ventana_calculadora.mainloop()

# Ejercicio 6: Diseñar un programa que utilice os para mostrar todos los archivos en un directorio.

import os
import tkinter as tk

def mostrar_archivos():
    listbox.delete(0, tk.END)
    archivos = os.listdir()
    
    for archivo in archivos:
        listbox.insert(tk.END, archivo)

ventana = tk.Tk()
ventana.title("Lista de Archivos")

listbox = tk.Listbox(ventana)
listbox.pack(fill=tk.BOTH, expand=True)

boton_actualizar = tk.Button(ventana, text="Actualizar", command=mostrar_archivos)
boton_actualizar.pack()

mostrar_archivos()

ventana.mainloop()

# Ejercicio 7: Construir una aplicación en tkinter para gestionar tareas pendientes.

import tkinter as tk

lista_de_tareas = []

def ingresar_tareas():
    tarea = caja_ingresar_tarea.get()
    if tarea:
        lista_de_tareas.append(tarea)
        caja_ingresar_tarea.delete(0, tk.END)
        mostrar_tareas()

def mostrar_tareas():
    listbox_tareas.delete(0, tk.END)
    for tarea in lista_de_tareas:
        listbox_tareas.insert(tk.END, tarea)

ventana = tk.Tk()
ventana.config(width = 300, height = 300)
ventana.title(":::: Gestión de tareas ::::")

etiqueta_ingresar_tarea = tk.Label(text = " Ingrese tarea:")
etiqueta_ingresar_tarea.place(x = 30, y = 30)
caja_ingresar_tarea = tk.Entry()
caja_ingresar_tarea.place(x = 110, y = 30,width = 150,height = 20 )

boton_ingresar_tarea = tk.Button(text = "Ingresar tarea", command = ingresar_tareas )
boton_ingresar_tarea.place(x = 30, y = 120)

boton_mostrar_tarea = tk.Button(text = "Mostrar tarea", command = mostrar_tareas )
boton_mostrar_tarea.place(x = 30, y = 150)

listbox_tareas = tk.Listbox(ventana)
listbox_tareas.place(x = 110, y = 120, width = 150, height = 100)

ventana.mainloop()

# ::::::::::::::::::::::::::::::::: FIN PORTAFOLIO :::::::::::::::::::::::::::::::::