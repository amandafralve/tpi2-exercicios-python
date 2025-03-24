# EXERCÍCIO 1
''' Ler o ano atual e o ano de nascimento de uma
pessoa. Calcular a idade. Escrever uma mensagem
que diga se ela poderá ou não votar este ano, se ele
tiver mais de 16 anos →USE IF '''

import datetime
x = datetime.datetime.now()

print("Descubra se você pode votar! ")
ano = int(input("Insira o ano de seu nascimento: "))

idade = (x.year) - ano

if idade > 16:
	print("Cidadão pode realizar votação. ")
else:
	print("Cidadão não poderá votar. Idade mínima de 16 anos. ")