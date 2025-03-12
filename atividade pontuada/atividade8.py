import os
os.system("clear") 

opçao =str(input(""""
\t cor   \t Preço
    "Verde\t R$10,00"
    "Azul\t R$20,00"
    "Amarelo\t R$30,00"
    "Vermelho \t R$40,00" 
Digite a opçao desejada:   """))

match opçao:
    case 'Verde':
        print ("Verde--R$10,00")
    case 'Azul':
        print("Azul--R$20,00")    
    case 'amarelo':
        print("Amarelo--R$30,00")
    case 'vermelho':
        print("Vermelho--R$40,00")