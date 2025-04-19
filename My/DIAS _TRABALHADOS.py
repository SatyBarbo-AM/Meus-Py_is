# Solicita a quantidade de dias trabalhados
dias_trabalhados = int(input("Quantos dias o funcionário trabalhou no mês? "))

# Constantes
horas_por_dia = 8
valor_por_hora = 205.52

# Cálculo do salário
salario = dias_trabalhados * horas_por_dia * valor_por_hora

# Exibe o resultado formatado
print(f"O salário do funcionário é R${salario:.2f}")
