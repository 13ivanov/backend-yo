from cgi import print_arguments


edad_roberta =20
if edad_roberta >=18:
    print("Si puede entrar a la discoteca")
else:
    print("No puedes entrar, anda al cine")


edad_martin =70
if edad_martin >=65:
    print("esa persona esta jubilada")
elif edad_martin >=18:
    print("esa persona es mayor de edad")
elif edad_martin >=0:
    print("esa persona es menor de edad")
else:
    print("edad imposible")

data = input("Hola, ingresa tu talla de polo: ")
print (type(data))

# dependiendo de la talla del polo hacemos lo sgte, si es xl:llegara a fin de mes, si es L o M solicitar color de polo, si es S indicar que solamente hay color morado

if data == "XL":
    print("llegara el fin de mes")
elif data == "M" or "L":
    input("ingresa el color de polo")
elif data == "S":
    print("solo tenemos color morado")
else:
    print("la talla es incorrecta")