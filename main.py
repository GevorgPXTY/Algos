import random
import time
import matplotlib.pyplot as plt
import numpy as np
k = 2
f = open('time.txt', 'w+')
f.close()
l = 3
n = 1000
for i in range (l):
    print(n)
    f = open('time.txt', 'a')
    c = "\n"+ "\n" + "Count " +str(n) + "\n"
    f.write(c)
    f.close()
    for i in range (k):
        vector1000 = []
        for i in range(n):
            vector1000.append(random.uniform(-1, 1))  #массив от -1 до 1
        #print(vector1000)  #вывод изначального массива

        start = time.time()     # начало таймера

        for i in range(n - 1):  # метод пузырька
            for j in range(n - i - 1):
                if vector1000[j] > vector1000[j + 1]:
                    vector1000[j], vector1000[j + 1] = vector1000[j + 1], vector1000[j]

        end = time.time()  # конец таймера
        ftime = "\n" + str((end - start)* 10 **3 )
        f = open('time.txt', 'a')
        f.write(ftime)
        f.close()
    n *= 2
        #print(vector1000, "\n", "The time of execution of above program is :", (end-start) * 10**3, "ms") #вывод сортировки и времени
