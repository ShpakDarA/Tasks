import numpy as np
print("Введите количество элементов массива: ")
n = int(input())
nums = np.zeros(n)
for i in range(n):
    print("Введите число массива №", i+1)
    nums[i] = int(input())
nums = [int(x) for x in nums]
median = np.median(nums)
res = 0
for i in range(n):
    tmp = abs(nums[i]-median)
    res += tmp
print("Минимальное количество шагов: ", int(res))