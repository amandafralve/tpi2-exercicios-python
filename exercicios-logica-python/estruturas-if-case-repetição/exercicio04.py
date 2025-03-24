''' Faça um algoritmo e que leia dois números e apresente a subtração do maior pelo menor número. →USE IF '''

numUm = float(input("Insira o primeiro número: "))
numDois = float(input("Insira o segundo número: "))
res = None

if numUm > numDois:
    res = numUm - numDois
elif numDois > numUm:
    res = numDois - numUm
else:
    print("Os números são iguais!")
    res = 0

print(f"Resultado: {res}")