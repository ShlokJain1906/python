import numpy as np
#8.1
mA = np.arange(1,5).reshape(2,2)
mB = np.arange(5,9).reshape(2,2)
print(mA)
print(mB)
#8.2
print("Matrix multiplication : ")
print(np.matmul(mA,mB))
print("Transpose of A : ")
print(np.matrix_transpose(mA))