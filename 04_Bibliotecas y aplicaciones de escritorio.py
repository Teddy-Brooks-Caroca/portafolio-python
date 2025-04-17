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