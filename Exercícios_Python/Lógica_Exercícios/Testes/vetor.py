import numpy as np
# numero = [10, 20, 30, 40, 50]

# for i in range(len(numero)):
#      print(i, numero[i])

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

vv = np.array(v1 + v2)

for i in vv:
    if i == 5:
        novo_vv = np.delete(vv, 2)
        print(novo_vv)


