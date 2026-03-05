#Distinguir o número maior e o menor.
n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 < n3:
    print(f"Número maior {n1} e número menor{n2}.")
elif n3 > n1 < n2:
    print(f"Número maior {n3} e número menor {n1}.")
else:
    print(f"Número maior {n2} e número menor {n3}.")