''' Um comerciante comprou um produto e quer vendêlo com um lucro de 45% se o valor da compra for menor
que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor da compra e
mostre o valor de venda para o produto. →USE IF '''

valorCompra = float(input("Insira o valor do produto comprado: "))

if valorCompra > 20:
    valorCompra += (0.45 * valorCompra)
elif 0 < valorCompra < 20:
    valorCompra += (0.3 * valorCompra)
else:
    print("Ops! Os valores inseridos são negativos. Revise")
    exit()

print(f"Valor de venda do produto: R${valorCompra:.2f}")
