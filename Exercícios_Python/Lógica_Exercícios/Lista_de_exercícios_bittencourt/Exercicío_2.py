#Desenvolva um programa onde o usuário informe a idade e se tem alguma doença
#crônica. Caso tenha alguma doença crônica, deve-se informar também o número de
#doenças. O valor da mensalidade do plano de saúde sofrerá um acréscimo conforme a
#tabela abaixo, e no final o programa tem que informar qual o valor total a ser pago na
#mensalidade.


idade = int(input("Me informe sua idade:"))
doenca = int(input("Você possui alguma doença crônica?"))

if idade >= 0 and idade <= 18:
    taxa_basica = idade * 83.15 
    add_por_doenca = 0 / 100 * doenca
    valor = taxa_basica + add_por_doenca
    print(f"<--CONTA-->\nTaxa básica: R${taxa_basica:.2f}.\nAdd por doença: R${add_por_doenca:.2f}.\nValor a ser pago: R${valor:.2f}")
    
elif idade >= 19 and idade <= 33:
    taxa_basica = idade * 133.88 
    add_por_doenca = 5 / 100 * doenca
    valor = taxa_basica + add_por_doenca
    print(f"<--CONTA-->\nTaxa básica: R${taxa_basica:.2f}.\nAdd por doença: R${add_por_doenca:.2f}.\nValor a ser pago: R${valor:.2f}")
    
elif idade >= 34 and idade <= 44:
    taxa_basica = idade * 203.73  
    add_por_doenca = 10 / 100 * doenca
    valor = taxa_basica + add_por_doenca
    print(f"<--CONTA-->\nTaxa básica: R${taxa_basica:.2f}.\nAdd por doença: R${add_por_doenca:.2f}.\nValor a ser pago: R${valor:.2f}")
    
elif idade >= 45 and idade <= 58:
    taxa_basica = idade * 312.44 
    add_por_doenca = 15 / 100 * doenca
    valor = taxa_basica + add_por_doenca
    print(f"<--CONTA-->\nTaxa básica: R${taxa_basica:.2f}.\nAdd por doença: R${add_por_doenca:.2f}.\nValor a ser pago: R${valor:.2f}")
    
elif  idade >= 58:
    taxa_basica = idade * 498.53 
    add_por_doenca = 30 / 100 * doenca
    valor = taxa_basica + add_por_doenca
    print(f"<--CONTA-->\nTaxa básica: R${taxa_basica:.2f}.\nAdd por doença: R${add_por_doenca:.2f}.\nValor a ser pago: R${valor:.2f}")

    
