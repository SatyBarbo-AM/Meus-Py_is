# Solicita a quantidade de Km percorridos
km_percorridos = float(input("Quantos Km o carro percorreu? "))

# Solicita a quantidade de dias de aluguel
dias_alugado = int(input("Por quantos dias o carro foi alugado? "))

# Calcula o preço total
preco_por_dia = 90.0
preco_por_km = 0.20
total_a_pagar = (dias_alugado * preco_por_dia) + (km_percorridos * preco_por_km)

# Exibe o valor total
print(f"O total a pagar é R${total_a_pagar:.2f}")
