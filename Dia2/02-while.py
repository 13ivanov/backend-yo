from operator import concat
from unicodedata import numeric


numero =10
# el while trabaja como un bucle que se realizara de manera automatica hasta que la condicion o condiciones dejen de ser verdaderas
while numero >0:
    print("numero positivo")
    print (numero)
    numero -=1

# do while no existe en python
#solicitar 5 digitos para la loteria pero estos no pueden ser mayor que 100 ni numeros negativos

# DRY > Don´t repeat yourself 
contador_numeros =1
while contador_numeros < 6:
    numero = int(input("ingresa el numero de la loteria: "))
    if not (numero >100 or numero < 0):
        contador_numeros += 1
        continue
    print("numero ingresado es invalido, vuelva a intentar")