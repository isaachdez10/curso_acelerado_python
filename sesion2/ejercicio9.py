'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio9.py
Autor: ..............
Action: programa que compara contraseña
'''
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")