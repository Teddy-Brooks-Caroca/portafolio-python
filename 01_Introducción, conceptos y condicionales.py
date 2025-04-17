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