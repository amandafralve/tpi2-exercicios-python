''' I) UMA EMPRESA DE DESENVOLVIMENTO DE SOFTWARES PAGA A SEU VENDEDOR UM FIXO DE R$1500 POR MÊS, 
MAIS UM BÔNUS DE R$50 POR SOFTWARE VENDIDO. FAÇA UM ALGORITMO QUE LEIA A QUANTIDADE DE SOFTWARES
VENDIDOS E CALCULE O SALÁRIO TOTAL DO FUNCIONÁRIO. '''

salario = 1500
qntVend = int(input("\nInsira a quantidade de softwares vendidos no mês: "))

bonus = qntVend*50
salAtual = salario + bonus

print("\n-- RECEBIMENTO SALÁRIO --\n SALARIO FIXO: R$1500,00\n"
      f" BÔNUS: R${bonus},00\n----------------------\n"
      f" SALÁRIO TOTAL: {salAtual}\n")