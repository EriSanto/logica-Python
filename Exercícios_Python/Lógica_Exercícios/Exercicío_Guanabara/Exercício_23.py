# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.



valo_casa = float(input("Me informe o valor da casa: "))
salario_comprador = float(input("Me informe o seu salário: "))
anos_pagar =  int(input("Me informe os anos a pagar: "))

prestacao = valo_casa / anos_pagar
mes = prestacao / 12
porcent_salario = prestacao * (30/100)

if salario_comprador <= porcent_salario:
    print(f"Para pagar uma casa de R${valo_casa} em {anos_pagar} anos a prestação será de R${mes}.\nEmprestimo Negado!")
else:
    print(f"Para pagar uma casa de R${valo_casa} em {anos_pagar} anos a prestação será de R${mes}.\nEmprestimo Sucedido!")

