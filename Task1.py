print("Введите значение числа n:")
n = int(input())
print("Введите значение числа m:")
m = int(input())
print("n =", n, "m =", m)
import numpy as np

arr = np.zeros(n)
for i in range(n):
    arr[i] = i + 1
run_ind = m - 1
start_ind = 0
path = []
flag = True
while (flag):
    if (run_ind >= n - 1):
        run_ind -= n
    if (run_ind != 0):
        path.append(int(arr[start_ind]))
        start_ind = run_ind
    else:
        flag = False
        path.append(int(arr[start_ind]))
    run_ind += m - 1
# path = [int(x) for x in path]
print("Полученный путь: ", path)
