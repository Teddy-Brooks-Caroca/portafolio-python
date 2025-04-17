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
