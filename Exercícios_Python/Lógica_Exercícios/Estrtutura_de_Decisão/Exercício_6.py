# pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
preço1 = float(input("Me informe o primeiro preço: "))
preço2 = float(input("Me informe o segundo preço: "))
preço3 = float(input("Me informe o terceiro preço: "))

if preço1 < preço2 and preço3:
    print(f"Você deve comprar o priemeiro intem, pois tem  o menor preço: R${preço1}.")
elif preço3 < preço1 and preço2:
    print(f"Você deve comprar o segundo intem, pois tem  o menor preço: R${preço3}.")
elif preço2 < preço1 and preço3:
    print(f"Você deve comprar o terceiro intem, pois tem  o menor preço: R${preço2}.")
