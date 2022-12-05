import numpy as np
import matplotlib.pyplot as plt

N = 30 # кол-во точек

inp1 = np.random.random(N) # создание входных данных для вышележащих точек
inp2 = inp1 + [np.random.randint(10)/10 for i in range(N)] + 0.1
C1 = [inp1, inp2]

inp1 = np.random.random(N) # создание входных данных для ннижележащих точек
inp2 = inp1 - [np.random.randint(10)/10 for i in range(N)] - 0.1
C2 = [inp1, inp2]

f = [0, 1] # разделяющая прямая

w = np.array([-1, 1]) # веса, их значение обусловлено коэфициентом прямой k, который должен быть -1(w1/w2 = -1)

for i in range(N):
    inp = np.array([C2[0][i], C2[1][i]]) # передаем данные из массива С2
    y = np.dot(w, inp) # умножаем на веса
    if y >= 0: # проверка к какому массиву принадлежит наша точка
        print("Точка выше прямой С1")
    else:
        print("Точка ниже прямой С2")

plt.scatter(C1[0][:], C1[1][:], s=15, c='green') # отображение массиво точек
plt.scatter(C2[0][:], C2[1][:], s=15, c='brown')
plt.plot(f, c='yellow') # отображение прямой
plt.show()