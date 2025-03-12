import os
os.system ("clear")

#entrada
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

#Processamento
 
soma = a + b

if soma < c:
      print(f"A+B igual a {soma}")
      print ("A+B é menor que c")
      
elif soma > c:
   print(f"A+B igual a {soma}")
   print ("A+B é maior que C")
else: 
    print(f"A+B igual a {soma}")
    print("A+B é igual a C")



#saida