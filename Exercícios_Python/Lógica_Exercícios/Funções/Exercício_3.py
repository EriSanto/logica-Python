def zoologico():

    animais = []

    print("Crie seu Zoológico!")

    while True:
        
        digite_animais = input("Adicione um animal: ")

        animais.append(digite_animais)

        print(animais)

        continuar = input("Deseja adicionar mais animais, s ou n? ")
        if continuar == 'n':

            pergunta = input("Deseja remover algum animal, s ou n? ")

            if pergunta == 's':

                pergunta = input("Qual animal? ")

                animais.remove(pergunta)

                print(f"Zoológico criado!\nAqui estão seus animais!\n{animais}")
                break
            else:

             print(f"Zoológico criado!\nAqui estão seus animais!\n{animais}")
             break
            
zoologico()
