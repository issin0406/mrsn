import numpy as np

list_arr = np.array([[0.2, 0.2, 0.3, 0.3], [0.2, 0.4, 0.1, 0.3], [0.2, 0.3, 0.1, 0.4], [0.1, 0.1, 0 , 0.8]])
list_arrx = np.array([[1, 0, 0, 0]])
list_arry = np.array([[0, 1, 0, 0]])
list_arrz = np.array([[0, 0, 1, 0]])
list_arrw = np.array([[0, 0, 0, 1]])

result = np.array([])

print("xについて計算します¥n")
print("1")
result = np.dot(list_arrx, list_arr)
print(result)

for i in range(9):
    result = np.dot(result, list_arr)
    print(i)
    print(result)
