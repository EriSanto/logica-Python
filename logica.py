n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 and n3:
    print(f"{n1} maior.")
elif n3 > n1 and n2:
    print(f"{n3} maior.")
else:
    print(f"{n2} maior.")
