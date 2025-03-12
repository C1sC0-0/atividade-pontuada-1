import os
os.system ("clear")

morango = int(input("Digite a quantidade de morango: "))
maca = int(input("Digite a quantidade de maçã: "))

if morango <= 5:
    valor_morango = morango * 2.5
if morango > 5:
    valor_morango = morango * 2.2
if maca <= 5:
    valor_maca = maca * 1.8
if maca > 5:
    valor_maca = maca * 1.5   
total_frutas = morango + maca
valor_total = valor_maca + valor_morango

if total_frutas > 10 or valor_total > 15:
    valor= valor_total * 0.9
    print (f"Ganhou desconto de 10%, valor final:{valor}")

else:
    print(f"Valor final: {valor_total}")
