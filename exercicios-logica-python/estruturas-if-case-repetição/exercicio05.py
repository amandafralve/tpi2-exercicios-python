# EXERCÍCIO 5
''' Elabore um algoritmo que leia o nome e altura e idade de duas pessoas e 
mostre os dados da pessoa mais alta. → USE IF '''

nomeUm = input("Insira o nome da pessoa 1: ")
alturaUm = float(input("insira a altura da pessoa 1: "))
nomeDois = input("Insira o nome da pessoa 2: ")
alturaDois = float(input("insira a altura da pessoa 2: "))

if alturaUm > alturaDois:
    print(f"{nomeUm} é a pessoa mais alta, com {alturaUm}. ")
elif alturaDois > alturaUm:
    print(f"{nomeDois} é a pessoa mais alta, com {alturaDois}m de altura. ")
else:
    print(f"As duas pessoas possuem a mesma altura, {alturaUm}")