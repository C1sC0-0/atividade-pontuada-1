import os
os.system("clear") 

combustivel = str(input("Digite o tipo de combustivel(A - alcool / G - gasolina): "))
litros = int(input("Digite a quantidade de litros: "))

match combustivel:
    case 'A'| 'a':
        if litros <= 25:
            valor = 3.79 * 0.98 * litros
            print(f"O desconto é de 2%, o total a pagar é {valor:.2f}")
        if litros >25:
            valor = 3.79 * 0.96 * litros
            print (f"O desconto é de 4%, o total a pagar é{valor:.2f}")
    case 'B'| 'b':
        if litros <= 25:
            valor = 6.59 * 0.97 * litros
            print(f"O desconto é de 3%, o total a pagar é {valor:.2f}")
        if litros >25:
            valor = 6.59 * 0.95 * litros
            print (f"O desconto é de 4%, o total a pagar é{valor:.2f}")
