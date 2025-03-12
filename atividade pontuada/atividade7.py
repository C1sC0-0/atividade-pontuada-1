import os
os.system("clear") 


nome = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço do produto"))
total =float(qtd*preco)

if qtd <= 5:
    pagar = total * 0.98
    print(f"O desconto é de 2%, total a pagar = {pagar}")
if qtd > 5 and qtd <= 10:
    pagar = total * 0.97
    print (f"O desconto é de 3%, o total a pagar é: {pagar}") 
if qtd > 10:
    pagar = total*0.95
    print(f"O desconto é de 5%, o total a pagar é: {pagar}")