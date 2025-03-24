''' faça um programa que leia a medida em metros e faça uma conversão, e apresente um menu para conversão:
"1 - Decímetros  2 - Centímetros  3 - Milímetros" '''

print("\n-- Conversor de medidadas de metros --")
metros = float(input("Insira a medida em metros: "))
unidade = int(input("Insira a unidade para converter:\n1 - Decímetros\n2 - Centímetros\n3 - Milímetros"))

match unidade:
	case 1:
		unConv = metros*10
		un = "dm"
	case 2:
		unConv = metros*100
		un = "cm"
	case 3:
		unConv = metros*1000
		un = "mm"
	case _:
		print("Opção inválida. Insira novamente ")
		exit()

print(f"{metros}m = {unConv}{un}")