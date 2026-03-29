#Calculo de salário com descontos.
vh = float(input("Me informe seu salário hora:"))
vm = float(input("Me informe as horas trabalhadas esses mês: "))

sb = vh * vm

des_ir = 11
des_inss = 8
des_s = 5

ir = sb * (des_ir / 100)
inss = sb * (des_inss/ 100)
s = sb * (des_s / 100)

l1 = sb - ir
l2 = l1 - inss
l3 = l2 - s
print(f"+ Salário Bruto:R${sb}. -IR(11%):R${ir:.2f}. -INSS(8%):R${inss:.2f}. -Sindicato(5%):R${s:.2f}. = Salário Liquido :R${l3:.2f}" )