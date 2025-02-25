### PORTAFOLIO PYTHON ###

## 1. Introducción, conceptos y condicionales

# Ejercicio 1: Crear un programa que pida al usuario su nombre y edad, 
# luego muestre un mensaje personalizado indicando si es mayor o menor de edad.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print(f"{nombre.upper()} usted es menor de edad")
elif edad > 18:
    print(f"{nombre.upper()} usted es mayor de edad")
else:
    print("Ingrese una edad permitida por el sistema")

# Ejercicio 2: Diseñar un programa que calcule el precio total de una compra, 
# aplicando descuentos según el monto.

precio = int(input("Ingrese el precio del producto: "))
porcentaje_descuento = int(input("Ingrese el descuento ofrecido: "))

descuento = (precio * porcentaje_descuento) / 100

precio_final = precio - descuento

print("==== DETALLE ====")
print(f"PRECIO ORIGINAL: ${precio}")
print(f"DESCUENTO: {porcentaje_descuento}%")
print(f"PRECIO FINAL: ${precio_final}")
print("==== === === ====")

# Ejercicio 3: Escribir un programa que convierta grados Celsius a Fahrenheit y viceversa, 
# con una opción de menú para elegir la conversión.

print(":::::: Conversor de temperatura ::::::")

while True:
    print("1.- Convertir a grados Celsius","\n"
          "2.- Convertir a grados Fahrenheit","\n"
          "3.- Salir")
    
    opcion = input("Ingrese una de las opciones: ")

    if opcion == "1":
        print(":::::::::::::::::::::::::::::::")
        print("Conversión Fahrenheit a Celsius")
        grados = int(input("Ingrese la temperatura a convertir: "))
        conversion_f_x_c = (grados - 32) * 5/9
        print(f"{grados}°f son {conversion_f_x_c}°c")
        print(":::::::::::::::::::::::::::::::")
    
    elif opcion == "2":
        print(":::::::::::::::::::::::::::::::")
        print("Conversión Celsius a Fahrenheit")
        grados = int(input("Ingrese la temperatura a convertir: "))
        conversion_c_x_f = (grados * 1.8) + 32
        print(f"{grados}°c son {conversion_c_x_f}°f")
        print(":::::::::::::::::::::::::::::::")

    elif opcion == "3":
        print(":::::: Gracias por usar el conversor ::::::")
        break

# Ejercicio 4: Crear un programa que determine si un número ingresado 
# por el usuario es positivo, negativo o cero.

numero_usuario = int(input("Ingrese un numero: "))

if numero_usuario > 0:
    print("Su número es positivo")
elif numero_usuario < 0:
    print("Su número es negativo")
else:
    print("Su numero es igual a 0")
    
# Ejercicio 5: Implementar un programa que identifique el mayor 
# de tres números ingresados por el usuario.

numero_1 = int(input("Ingrese primer número: "))
numero_2 = int(input("Ingrese segundo numero: "))
numero_3 = int( input("Ingrese tercer número: "))

if numero_1 > numero_2 and numero_3:
    print("el primer número es el mayor")
elif numero_2 > numero_1 and numero_3:
    print("el segundo número es el mayor")
else:
    print("el tercer número es el mayor")
    
# Ejercicio 6: Diseñar un menú interactivo que permita seleccionar 
# opciones como "Sumar", "Restar" o "Salir".

print("::::: CLACULADORA SIMPLE :::::")
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


# Ejercicio 7: Simular un sistema de autenticación básico que 
# valide un usuario y contraseña predefinidos.

nombre_usuario = input("Ingrese su nombre: ")
contraseña = input("Ingrese su contraseña: ")

nombre_usuario = nombre_usuario.lower().replace(" ","")

if nombre_usuario == "johndoe":
    if contraseña == "071085":
        print("usuario y contraseña válidos")
    else:
        print("su contraseña no es válida")
else:
    print("su usuario no es válido")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## 2. Entrada de datos, bucles y listas

# Ejercicio 1: Crear un programa que sume todos los números 
# introducidos por el usuario hasta que se ingrese un "0".

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

# Ejercicio 2: Escribir un programa que genere una lista 
# de números del 1 al 10 y los imprima en orden inverso.

lista_de_numeros = []

for n in range(1,11):
    lista_de_numeros.append(n)

print(lista_de_numeros[::-1]) # primer método

lista_de_numeros.reverse() # segundo método
print(lista_de_numeros)

# Ejercicio 3: Implementar un programa que calcule el promedio
# de una lista de números ingresados por el usuario.

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

Ejercicio 5: Diseñar un sistema para ingresar y almacenar nombres en una lista, con opción de eliminar duplicados.
Ejercicio 6: Generar una tabla de multiplicar usando bucles anidados.
Ejercicio 7: Construir un programa que simule un cajero automático con saldo inicial, depósitos y retiros.
3. Colecciones, diccionarios y funciones
Ejercicio 1: Crear una función que reciba una lista y devuelva el elemento más grande y el más pequeño.
Ejercicio 2: Escribir un programa que use un diccionario para almacenar la relación entre nombres y edades, y permita buscar datos.
Ejercicio 3: Implementar una función que calcule la suma de los valores en un diccionario.
Ejercicio 4: Diseñar una función que reciba una tupla de números y devuelva su promedio.
Ejercicio 5: Crear un programa que almacene notas de estudiantes en un diccionario y calcule el promedio de cada uno.
Ejercicio 6: Implementar un programa que permita registrar tareas pendientes en un diccionario con categorías.
Ejercicio 7: Crear un generador de contraseñas aleatorias utilizando colecciones.
4. Bibliotecas y aplicaciones de escritorio
Ejercicio 1: Crear un script que use la biblioteca math para resolver ecuaciones cuadráticas.
Ejercicio 2: Diseñar un programa que utilice random para simular el lanzamiento de un dado.
Ejercicio 3: Escribir un programa que genere un gráfico de barras con datos ficticios usando matplotlib.
Ejercicio 4: Implementar un programa que use tkinter para crear una interfaz que permita sumar dos números.
Ejercicio 5: Crear una pequeña calculadora gráfica con operaciones básicas usando tkinter.
Ejercicio 6: Diseñar un programa que utilice os para mostrar todos los archivos en un directorio.
Ejercicio 7: Construir una aplicación en tkinter para gestionar tareas pendientes.