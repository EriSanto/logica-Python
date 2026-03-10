#Calculo de salário com descontos.
vh = float(input("Me informe seu salário hora:"))
vm = float(input("Me informe as horas trabalhadas esses mês: "))

sb = vh * vm

ir = sb * (11 / 100)
inss = sb * (8 / 100)
s = sb * (5 / 100)

l1 = sb - ir
l2 = l1 - inss
l3 = l2 - s
print(f"+ Salário Bruto:R${sb}. -IR(11%):R${ir}. -INSS(8%):R${inss}. -Sindicato(5%):R${s}. = Salário Liquido :R${l3}" )