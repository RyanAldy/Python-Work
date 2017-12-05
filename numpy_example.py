import numpy as np

A = [1,2,3,4,5]
B = [10,20,30,40,50]

L1 = np.array(A)
L2 = np.array(B)

# Will add first element of first list with first element of 2nd list etc
L3 = L1 + L2
# Will multiply first element of first list with first element of 2nd list etc
L4 = L1 * L2

print(L3)
print(L4)
