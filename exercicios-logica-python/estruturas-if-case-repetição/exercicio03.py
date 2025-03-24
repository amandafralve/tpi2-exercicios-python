''' Construa um programa que LEIA dois números reais e leia um dos seguintes símbolos: +, -, * ou /. De acordo
com o símbolo escolhido, deverá ser feita a operação. O referido programa deve retornar o resultado da
operação selecionada. Exemplo: case "+": soma = numero1 + numero2 → USE CASE '''

print("Cálculo de 2 números")
numUm = float(input("Insira o primeiro número: "))
numDois = float(input("Insira o segundo número: "))
operador = int(input("Insira o operador a ser usado:\n1. Adição(+)\n2. Subtração(-)\n3. Multiplicação(*)\n4. Divisão(/) "))
res = None

match operador:
    case 1:
        res = numUm + numDois
    case 2:
        res = numUm - numDois
    case 3:
        res = numUm * numDois
    case 4:
        if numDois == 0:
            print("Não é possível dividir por zero.")
            exit()
        res = numUm / numDois
    case _:
        print("Opção inválida. Tente novamente")
        exit()

print(f"O resultado do cálculo é: {res}")