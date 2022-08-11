'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio8.py
Autor: ..............
Action: detecta numero negativos
'''
numero = int(input("Escriba un número positivo o negativo: "))
if numero > 0:
 print(f"Escribio un numero positivo {numero}")
elif numero < 0:
  print(f"Escribio un numero negativo {numero}")
else:
 print("El numero es neutro")   
 print(f"Ha escrito el número {numero}")