# lista = [2,3,4,5,6,7,8,]
# palavra = 'Eriky'
# for letra in palavra:
#     print(letra)

#função range server para ir de um ponto para outro sem sequência.
#or numero in range(1,11):
#   print(numero)

#repetição da valor
# nome = input("Digite seu nome:")
# for x in range(10):
#    print(f'{x+1} {nome}')
   
#range(valor_inicial, valor_final, incremento)
'''Se adicionar mais um número no range, ele começa a conta de com forme o o ultimo
número apresentado'''
'''crescimento'''
# for x in range(2,20,2):
#    print(x)
   
# '''decrimento'''
# for x in range(20,2,-2):
#    print(x)

'''pedras = ('Rubi', 'Esmeralda', "Quartzo", 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
   if pedra == "Quartzo":
    continue
   print(pedra)'''
   
'''nomes = ("Eriky","Leticias","Lucas")

for nome in nomes:
   if nome == "Eriky":
      continue
   print(nome)'''
   
'''numeros = ('1','2','3')

for numero in numeros:
   if numero == "2":
      continue
   print(numero)'''
   
'''for titulo in range(1,6):
   print("Titulo", titulo)
   for nomes in range(2):
      print("Maria" , nomes)'''
 

# pedras = ('Rubi', 'Esmeralda', "Quartzo", 'Safira', 'Diamante', 'Turmalina')

# for pedra in pedras:
#    if pedra == "Quartzo":
#     continue
#    print(pedra)
   
   
# numero = [1,2,3,4,5,6,7,8]

# for n in numero:
#    if n  % 2 != 0:
#     continue
#    print(f"Esse {n} é par")
   
   
nomes = ("Eriky", "Leticia", "Maria")

for n in nomes:
   for a in range(1,5):
    print(a , n)