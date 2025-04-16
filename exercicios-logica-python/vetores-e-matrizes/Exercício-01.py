# 1. Crie um vetor leia 10 posições de números inteiros, armazene os valores e mostre.
tamanho = 10
vetor = []

for i in range (tamanho):
	elemento  = int(input(f"Digite um número. Ele é o elemento {i+1} do vetor: "))
	vetor.append(elemento)
	
print("Vetores:", vetor)