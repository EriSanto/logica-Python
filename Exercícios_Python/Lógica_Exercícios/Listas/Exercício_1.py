# x = 0
# pessoa = []


# while True:
    
#     atributo = input("Digite um atrubuto: ")
    
#     add_atributo = pessoa.append(atributo)
#     x +=1
    
#     print(pessoa)
    
#     continuar = input("Deseja continuar? s ou n ? ")
#     if continuar == 'n':
#         print(pessoa)
#         break
    

animais = ["Cachorro","Gato","Papagaio","Tartaruga"]

# remove_item = lista.remove("Cachorro")
# add_item = lista.append("Porco")



for animal in animais:
    if animal.startswith('C'):
        animais[2] = animais[2].upper()
        continue
    print(animal)
    
