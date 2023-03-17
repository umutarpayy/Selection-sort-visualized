import matplotlib.pyplot as plt
import numpy as np

amount = 15
rand_list = np.random.randint(0, 100, 15)
x = np.arange(0, amount, 1)
n = len(rand_list)
for i in range(n):
    for j in range(i, n):
        plt.bar(x, rand_list)
        plt.pause(0.01)
        plt.clf()
        if rand_list[i] > rand_list[j]:
            rand_list[i], rand_list[j] = rand_list[j], rand_list[i]
#plt.show()
