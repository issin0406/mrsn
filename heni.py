import numpy as np

np.set_printoptions(precision=12)

list_arr = np.array([[0.1, 0.5, 0.1, 0.3], [0.2, 0.4, 0.2, 0.2], [0, 0.3, 0.2, 0.5], [0.4, 0.1, 0.3 , 0.2]],
dtype='float64')
list_arrx = np.array([[1, 0, 0, 0]],dtype='float64')
list_arry = np.array([[0, 1, 0, 0]],dtype='float64')
list_arrz = np.array([[0, 0, 1, 0]],dtype='float64')
list_arrw = np.array([[0, 0, 0, 1]],dtype='float64')


result = np.array([])

print("xについて計算します¥n")
print("初期値")
result = list_arrx
print(result)


for i in range(10):
    result = np.dot(result, list_arr)
    print("w" + str(i+1) )
    print(result)


print("")

print("yについて計算します¥n")
print("初期値")
result = list_arry
print(result)


for i in range(10):
    result = np.dot(result, list_arr)
    print("w" + str(i+1) )
    print(result)


print("")


print("zについて計算します¥n")
print("初期値")
result = list_arrz
print(result)


for i in range(10):
    result = np.dot(result, list_arr)
    print("w" + str(i+1) )
    print(result)


print("")

print("wについて計算します¥n")
print("初期値")
result = list_arrw
print(result)


for i in range(10):
    result = np.dot(result, list_arr)
    print("w" + str(i+1) )
    print(result)
