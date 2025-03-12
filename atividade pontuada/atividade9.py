import os
os.system("clear") 

renda= float(input("Digite a renda mensal: "))
emprestimo= float(input("Digite o valor do emprestimo solicitado: "))
prestacoes= int(input("Digite o numero de parcelas: "))
valor_parcelas= emprestimo/prestacoes

if emprestimo <= (10*renda) and valor_parcelas <= (0.30*renda):
    print("Emprestimo concedido!")
else:
    print("EMprestimo negado!")
                                                   