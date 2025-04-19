print('Bem Vindo ao conversor de milhar a kilometros')

print('Escreva um numero em milhas: ')
milhas = input() #string

print('Tipo de dado de milhas', type(milhas))
# Converter de string para numero.
milhas = float(milhas)
print('Tipo de dado de milhas', type(milhas))

# 1 milha = 1.609 kms
kilometros = milhas * 1.609

print("Millas ingresadas:", milhas)
print("Kilómetros:", kilometros)
