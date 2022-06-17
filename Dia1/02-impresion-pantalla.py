curso="Backend"
print(curso)
dia= 16
#cuando dos valores son texto hara una concatenacion
print("El curso es "+curso)
print("el curso es", curso)
#el + no sirve para unir texto y numero ya que se confunde si se concatena o suma
print("el curso es "+curso+" y el dia es ",dia)

#Window + . > menu emergente con emoticones

print("el curso es {} y el dia es {}".format(curso,dia))  #por cada {} hay una variable en format

print("el curso es {1} y el dia es {0}".format(curso,dia))  #si queremos que la varible escrita 2da aparezca prmero en el print