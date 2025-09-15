import numpy as np
# 5.1
arr = np.arange(10,26).reshape(4,4)
print(arr)
# 5.2
print("Second row : ",arr[1])
print("Last column : ",arr[:,-1])
# 5.3
arr[0] = 0
print("After editing : ")
print(arr)