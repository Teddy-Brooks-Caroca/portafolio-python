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


mulltiplicando = int(input("Ingrese la tabla que desea: "))            # MÉTODO TRADICIONAL, SIN ANIDADO
multiplicador = int(input("Ingrese hasta que numero desea la tabla: "))

for n in range(1,multiplicador + 1):
    print(f"{mulltiplicando} x {n} = {mulltiplicando * n}")

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

numeros_a_sumar = {}

def sumar_elementos(conjunto):
    return sum(numeros_a_sumar[conjunto])

def mostar_diccionario(diccionario):
    for conjunto,valor in diccionario.items():
        print(f"{conjunto}:{valor}")    

while True:

    conjunto = input("Ingrese 'conjunto' seguido de una letra a la lista o escriba 'salir': ")

    if conjunto.lower() == "salir":
        mostar_diccionario(numeros_a_sumar)
        print("Usted ha salido del programa")
        print(":::::::::::::::::::::::::::::::::::::")
        break

    else:
        valor = int(input("Ingrese un nuevo valor a la lista: "))
        print(":::::::::::::::::::::::::::::::::::::")

        if conjunto not in numeros_a_sumar:
            numeros_a_sumar[conjunto] = []
            numeros_a_sumar[conjunto].append(valor)

        while True:

            confirmacion_nuevo_valor = input("¿Desea agregar un nuevo valor?(si/no): ")
            print(":::::::::::::::::::::::::::::::::::::")

            if confirmacion_nuevo_valor == "si":

                nuevo_valor = int(input("Ingrese nuevo valor: "))
                numeros_a_sumar[conjunto].append(nuevo_valor)
            
            else:
                print("Fin de los valores para este conjunto")
                print(":::::::::::::::::::::::::::::::::::::")
                break

conjunto_a_sumar = input("Ingrese 'conjunto' seguido de su letra para sumar sus elementos: ")
print(":::::::::::::::::::::::::::::::::::::")

if conjunto_a_sumar in numeros_a_sumar:
    resultado = sumar_elementos(conjunto_a_sumar)
    print(f"La suma de los valores del conjunto {conjunto_a_sumar} es: {resultado}")
    print(":::::::::::::::::::::::::::::::::::::")
else:
    print("Conjunto no se encuentra")
    print(":::::::::::::::::::::::::::::::::::::")

# Ejercicio 4: Diseñar una función que reciba una tupla de números y devuelva su promedio.
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