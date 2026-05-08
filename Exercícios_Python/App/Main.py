class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "115555-7777")
conta = Conta(c1.nome,6565,0)

print(c1.nome," Numero: ",conta.numero, "Seu Saldo: ",conta.saldo)