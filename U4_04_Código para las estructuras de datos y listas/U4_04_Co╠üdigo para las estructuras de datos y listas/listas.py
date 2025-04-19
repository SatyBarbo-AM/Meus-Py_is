nombres = ["Rodrigo", "Juan", "Pedro", "Santiago", "Jorge", "Raymundo"]
print(nombres)
#f-strings
for i, nombre in enumerate(nombres):
    #print("Se inscribió ", i, "en la lista:", i, nombre)
    print( f"Se inscribió {nombre} en la lista con el índice {i}" )

print( "Bienvenidos a la fiesta", nombres[:3] )
print( "Lo sentimos", nombres[3:])