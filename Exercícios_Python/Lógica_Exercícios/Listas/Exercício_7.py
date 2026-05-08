#Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []

x = 0

a = 0
e = 0
i = 0
o = 0
u = 0

while x < 10:
    x +=1
    
    print("Digite letras")
    letra = input('')
    
    letras.append(letra)
   
 
for l in letras: 
    if l == "a":
        a+=1
        letras.remove(l)
for l in letras: 
    if l == "e":
        e+=1
        letras.remove(l)
for l in letras: 
    if l == "i":
        i+=1
        letras.remove(l)
for l in letras:
    if l == "o":
        o+=1
        letras.remove(l)
for l in letras:
    if l == "u":
        u+=1
        letras.remove(l)
        
cosoantes = x - a - e - i - o - u 
print(f"Cosoantes lidas: {cosoantes} ")
print(letras)

         



