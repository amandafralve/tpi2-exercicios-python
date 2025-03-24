''' > Faça um algoritmo para ler: nome do cliente e valor do depósito. Calcular e escrever o saldo atual (saldo_atual = 800 + deposito). 
Também testar se saldo atual é igual a zero, escrever a mensagem "Saldo Limite"; se for acima de zero, escrever a mensagem "Saldo Positivo"; 
senão, escrever a mensagem "Saldo Negativo". Mostre o nome do cliente e valor do saldo atual. →USE IF'''

nomeCliente = input("Insira o nome do cliente: ")
deposito = float(input("Insira o valor do depósito: "))

saldo_atual = 800 + deposito

if saldo_atual == 0:
	print("Saldo LIMITE")
elif saldo_atual > 0:
    print("Saldo POSITIVO")
else:
    print("Saldo NEGATIVO")

print(f"CLIENTE: {nomeCliente}\nSALDO: R${saldo_atual:.2f}")