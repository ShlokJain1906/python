import numpy as np
#10.1
arr = [[2,1,3],[0,5,6],[7,8,9]]
print(arr)
#10.2
print("Deterinant : ")
print(np.linalg.det(arr))
print("Inverse : ")
print(np.linalg.inv(arr))
print("Eigen values and Eigen vector : ")
eigval,eigvec = np.linalg.eig(arr)
print(eigval)
print(eigvec)
