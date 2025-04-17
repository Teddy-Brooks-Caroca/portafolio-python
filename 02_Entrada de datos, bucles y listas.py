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
