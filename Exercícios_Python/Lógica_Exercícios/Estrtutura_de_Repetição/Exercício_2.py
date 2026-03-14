# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Me informe seu nome:")
senha = input("Me informe sua senha?:")

while senha == nome:
 print("A senha não pode ser igual ao nome! Ensira uma nova senha.")
 int(input("Senha:"))
 break