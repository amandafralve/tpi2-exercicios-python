''' 4) FAÇA UM ALGORITMO E O FLUXOGRAMA QUE LEIA O ANO DE NASCIMENTO DE UMA PESSOA, E LEIA O NOME DA 
PESSOA E ESCREVA QUANTOS ANOS ESSA PESSOA TEM , E MOSTRE O NOME DIGITADO. '''

nome = input("Insira o nome da pessoa: ")
anoNasc = int(input("Insira o ano de nascimento: "))
anoHoje = int(input("Insira em que ano estamos: "))

idade = anoHoje - anoNasc
print(f"{nome} possui {idade} anos.")


