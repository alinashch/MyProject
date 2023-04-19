import entropy as entropy
import numpy as np
import random as rd
import networkx as nx
import numpy as np
from scipy import spatial
import time
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import entropy

import matplotlib.pyplot as plt

num_points=40

points_coordinate = np.random.rand(num_points, 2) * 100
print(points_coordinate)


distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
print(distance_matrix)


def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


def lengthCal(antPath, distmat):  # Рассчитать расстояние
    length = []
    dis = 0
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            dis += distmat[antPath[i][j]][antPath[i][j + 1]]
        dis += distmat[antPath[i][-1]][antPath[i][0]]
        length.append(dis)
        dis = 0
    return length

antEnter = 120                  # Не номер
alpha = 1                     # Фактор важности феромона
beta = 3                      # Фактор важности эвристической функции
pheEvaRate = 0.3              # Скорость испарения феромона
cityNum = distance_matrix.shape[0]
pheromone = np.ones((cityNum,cityNum))                   # Феромоновая матрица
heuristic = 1 / (np.eye(cityNum) + distance_matrix) - np.eye(cityNum)       # Матрица эвристической информации, дубль 1 / дизмат
iter,itermaxMY = 1,100
Emax = 0

for i in range(len(heuristic[0])):
    for k in range(len(heuristic)):
        if heuristic[i][k] != 0:
            Emax += entropy(heuristic[i][k], base=10)


while iter < itermaxMY:
    antPathMY = np.zeros((antEnter, cityNum)).astype(int) - 1  # Путь муравья
    firstCity = [i for i in range(cityNum)]
    rd.shuffle(firstCity)  # Случайно назначьте начальный город для каждого муравья
    unvisted = []
    p = []
    pAccum = 0
    Ecurr = 0
    for i in range(cityNum):
        antPathMY[i][0] = firstCity[i]
    for i in range(len(antPathMY[0]) - 1):  # Постепенно обновляйте следующий город, в который собирается каждый муравей
        for j in range(len(antPathMY)):
            for k in range(cityNum):
                if k not in antPathMY[j]:
                    unvisted.append(k)
            for m in unvisted:
                pAccum += pheromone[antPathMY[j][i]][m] ** alpha * heuristic[antPathMY[j][i]][m] ** beta
            for n in unvisted:
                p.append(pheromone[antPathMY[j][i]][n] ** alpha * heuristic[antPathMY[j][i]][n] ** beta / pAccum)
                Ecurr += entropy(p, base=10)
            roulette = np.array(p).cumsum()  # Создать рулетку
            r = rd.uniform(min(roulette), max(roulette))
            for x in range(len(roulette)):
                if roulette[x] >= r:  # Используйте метод рулетки, чтобы выбрать следующий город
                    antPathMY[j][i + 1] = unvisted[x]
                    break
            E = 1
            if Emax != 0:
                E = 1 - (Emax - Ecurr) / Emax
            if E >= 0.85:
                beta = 5
            elif 0.65 <= E < 0.85:
                beta = 4
            elif 0.45 <= E < 0.65:
                beta = 3
            elif E < 0.45:
                beta = 2
            unvisted = []
            p = []
            pAccum = 0
    pheromone = (1 - pheEvaRate) * pheromone  # Феромон летучий
    length = lengthCal(antPathMY, distance_matrix)


    for i in range(len(antPathMY)):
        for j in range(len(antPathMY[i]) - 1):
            pheromone[antPathMY[i][j]][antPathMY[i][j + 1]] += 1 / length[i]  # Обновление феромона
        pheromone[antPathMY[i][-1]][antPathMY[i][0]] += 1 / length[i]
    iter += 1
def enterMy(ant, iter):
    global antEnter
    antEnter=ant
    global itermaxMY
    itermaxMY=iter


def column(matrix, i):
    return [row[i] for row in matrix]

def findCorrectPathMy(arr):
    a = num_points + 1
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * 3
    for i in range(len(distance_matrix)):
        for j in range(len(arr)):
            if i == j:
                mas[i][0] = arr[j]
                mas[i][1] = distance_matrix[i][0]
                mas[i][2] = distance_matrix[i][1]
    mas[num_points][0] = arr[0]
    mas[num_points][1] = distance_matrix[0][0]
    mas[num_points][2] = distance_matrix[0][1]
    return  mas


def read_all_lines(filename):
    with open(filename) as file:
        return file.readlines()
if __name__ == '__main__':
    result = []
    lines = read_all_lines("city.txt")
    for line in lines:
        result.append(list(map(lambda x: float(x), line.split())))

    enterMy(50, 100)



