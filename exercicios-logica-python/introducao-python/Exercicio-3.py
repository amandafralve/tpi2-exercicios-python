''' 3) FAÇA UM PROGRAMA QUE LEIA UMA TEMPERATURA EM GRAUS CELSIUS E CONVERTA-A PARA GRAUS FAHRENHEIT.
A FÓRMULA DE CONVERSÃO É: F <- C * 1.8 + 32 SENDO F A TEMPERATURA EM FAHRENHEIT E C A TEMPERATURA EM CELSIUS. '''

print("Conversão de Celsius (C°) para Fahrenheit (F)\n")
celsius = float(input("Insira o valor ta temperatura me Celsius:"))

fahrenheit = (celsius * 1.8) + 32

print("CONVERSOR CELSIUS PARA FAHRENHEIT\n"f"{celsius}C° = {fahrenheit}F")