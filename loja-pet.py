print('+++++++++++++++++++++++++++++++++++++++++++"')
print('++    BEM VINDOS A                        ++')
print('++    Loja de PETS MANAUS                 ++')
print('++++++++++++++++++++++++++++++++++++++++++++')

num_caes = 10
num_gatos = 8
num_passaros = 25

Total_Animais = num_caes + num_gatos + num_passaros

print('Por favor, escreva seu nome')
nome = input() 
print('Por favor, escreva seu sobrenome')
sobrenome = input()

# Concatenação
nome_completo = nome + " " + sobrenome

print('Obrigado por nos visitar', nome_completo)
print('Atualmente contamo com: ')
print('Caes:', num_caes, 'Gatos:', num_gatos, 'Passaros:', num_passaros)
print('Em total teremos', Total_Animais, 'caAnimais')

