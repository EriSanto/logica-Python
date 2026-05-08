#Faça um programa para exibir e calcular a soma dos N primeiros termos da sequência
#de Fibonacci. Esta sequência começa com os termos 1 e 1 e, a partir do terceiro termo,
#os termos são calculados pela soma dos dois termos anteriores: 1, 1, 2, 3, 5, 8, 13, 21,
#34, ...


# print('{}'.format(c), end=' ')
n = 8

n1= 0
n2 = 1
n3= 0

cont = 1

while cont < n:
    
    print('{}'. format(n3), end=' ' )
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    cont+=1

print("fim")

 
 
 
  
    
    





