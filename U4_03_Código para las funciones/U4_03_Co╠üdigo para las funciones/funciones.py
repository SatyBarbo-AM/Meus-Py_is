#Pre-definidas print(), type(), range(), input()

def saludar(nombre):
    print("Hola", nombre)

#Celsius a Fahrenheit: (C * 1.8) + 32
def convertir_a_fahrenheit(c):
    return (c * 1.8) + 32
    
#saludar("Rodrigo")
#saludar("Juan")
#saludar("Sergio")

print( convertir_a_fahrenheit(10) )
print( convertir_a_fahrenheit(30) )
print( convertir_a_fahrenheit(80) )