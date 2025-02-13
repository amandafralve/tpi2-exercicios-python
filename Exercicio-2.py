''' 2) ANALISANDO A FORMULA: VALORATRASO = VALOR + (VALOR * (TAXA/100) *TEMPO),
CRIE UM ALGORITMO PARA EFETUAR O CALCULO DO VALOR DE UMA PRESTAÇÃO EM ATRASO. 
LEIA O VALOR DA PRESTAÇÃO E A TAXA DE JUROS IMPOSTA PELO BANCO, E LEIA
A QUANTIDADE DE MESES EM ATRASO. (TEMPO) '''

prestacao = float(input("Insira o valor da Prestação: "))
taxaJuros = float(input("Insira o valor da taxa imposta pelo banco: "))
mesAtraso = int(input("Insira a qauntidade de meses em atraso: "))

valorAtraso = prestacao + (prestacao * (taxaJuros/100) * mesAtraso)

print(f"FICHA PAGAMENTO\n VALOR PARCELA: R${prestacao:.2f}\n"
      f" MESES EM ATRASO: {mesAtraso}\n" f" JUROS: {taxaJuros}\n"
    f" PREÇO TOTAL PRESTAÇÃO: R${valorAtraso}")