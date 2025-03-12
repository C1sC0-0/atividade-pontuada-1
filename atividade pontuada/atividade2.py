import os
os.system ("clear")

nome = input("Digite seu nome: ")
sexo = input ("Digite seu genero: ") 
estado = input ("Digite seu estado civil: ")
match sexo:
     case f:
          if estado == 'casada' :
               tempo = str(input("Digite seu tempo de casada: "))

print (f"seu nome é:{nome}")
print (f"seu genero é:{sexo}")
print (f"seu estado civil é:{estado}")
