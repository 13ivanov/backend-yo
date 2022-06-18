#operadores aritmeticos
edad_arleth=26
edad_ariatna=19

#SUMA
print("la suma es", edad_arleth+edad_ariatna)

#RESTA
print(edad_arleth-edad_ariatna)

#MULTIPLICACION
print(edad_arleth*edad_ariatna)

#DIVISION
print(edad_arleth/edad_ariatna) #el resultado es con decimales

#MODULO
print(edad_arleth % edad_ariatna) #el modulo es el resultado entero de la division

#COCIENTE 
print(edad_arleth // edad_ariatna)  #es el resultado de la division pero sin decimales

#POTENCIA
print(edad_ariatna ** 0)

#EN EL CASO DE LOS CARACTERES STRING
#cuando hacemos una sumatoria con el string se hace una concatenacion


mes="Junio"
temporada ="invierno"
print(mes+temporada)
#y si hacemos uso de la multiplicacion hara que se repita n canticdad de veces
print(mes*5)


#Operadores de asignacion

#operadores comparacion
#MAYOR QUE
print(edad_arleth>edad_ariatna)

#MENOR QUE
print(edad_ariatna<edad_arleth)

# == igual que
print(edad_ariatna==edad_arleth)

# != diferente que
print(edad_arleth!=edad_ariatna)

# mayor o igual que
print(edad_arleth>=edad_ariatna)

# menor o igual que
print(edad_ariatna<=edad_arleth)


#OPERADORES LOGICOS
# and Y   basta con que uno sea falso para que sea falso
print(edad_ariatna>18 and edad_arleth > edad_ariatna)

# or O     basta con que uno sea verdadero para que todo sea verdadero
print(edad_ariatna <18 or edad_ariatna > edad_arleth)

# not NO     invierte el resultado
print(not edad_arleth > 50)

# Ejercicios
edad_eduardo= 18
edad_renato = 26
edad_laura = 35


# Como saber si eduardo es mayor de edad
print("eduardo es mayor de edad", edad_eduardo>=18)
# Como saber si eduardo es mayor que laura
print(edad_eduardo>edad_laura)
# Como saber si renato es menor que laura pero mayor que eduardo
print(edad_renato<edad_laura and edad_renato>edad_eduardo)
# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura>edad_renato or edad_laura<edad_eduardo)


# Operadores de asignacion
# = Asignacion
edad=50

# Incremento
edad +=1

#  Decremento
edad -=1

# Multiplicador
edad *=1
# Division
edad /=2
