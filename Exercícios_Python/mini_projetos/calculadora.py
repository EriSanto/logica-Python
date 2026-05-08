op = ' '

while True:
     n1 = int(input("Ensira um número interio: "))
     op = input("Ensira um operador: ")

     while op != "+" and op != "-" and  op !="*" and  op !="/":
          op = input("Ensira um operador correto: ")
          
     n2 = int(input("Ensira um segundo número inteiro: "))
          
     if op == '+':
      print(f"Resultado:\n{n1} + {n2} = {n1+n2}")
               
           
     elif op == '-':
      print(f"Resultado:\n{n1} - {n2} = {n1-n2}")
      

     elif op == '*':
      print(f"Resultado:\n{n1} * {n2} = {n1*n2}")  
      

           
     elif op == '/':
      print(f"Resultado:\n{n1} / {n2} = {n1/n2}")
      

     
     cont = input("Deseja continuar? ")
     if cont == 'Não' or  cont == 'não' or cont ==  'N' or cont ==  'n':    
      print("Obrigado por testar! :)\nAté logo!")
      break
       

    