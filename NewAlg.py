import re

import CommonAlg
import numpy as np
import random as rd
import networkx as nx
import numpy as np
from scipy import spatial
import time
import matplotlib.pyplot as plt
import pandas as pd
from CommonAlg import CommonAlg

import matplotlib.pyplot as plt


def read_all_lines(filename):
    with open(filename) as file:
        return file.readlines()


def enterCoor(num_points):
    points_coordinate = np.random.rand(num_points, 2) * 100
    return points_coordinate


def enterFile():
    result = []
    lines = read_all_lines("city.txt")
    for line in lines:
        result.append(list(map(lambda x: float(x), line.split())))
    return result


# num_points=10

def cal_distance_matrix():
    i = enterFile()
    distance_matrix = spatial.distance.cdist(i, i, metric='euclidean')
    return distance_matrix


def cal_total_distance(routine):
    num_points, = routine.shape
    return sum(
        [cal_distance_matrix()[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


def lengthCal(antPath, distance_matrix):
    length = []
    dis = 0
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            dis += distance_matrix[antPath[i][j]][antPath[i][j + 1]]
        dis += distance_matrix[antPath[i][-1]][antPath[i][0]]
        length.append(dis)
        dis = 0
    return length


def alg(antNum, alpha, beta, pheEvaRate, distance_matrix, itermax):
    cityNum = distance_matrix.shape[0]
    pheromone = np.ones((cityNum, cityNum))
    heuristic = 1 / (np.eye(cityNum) + distance_matrix) - np.eye(cityNum)  # Матрица эвристической информации, дубль 1 / дизмат
    iter = 1
    history = [None]*itermax
    while iter < itermax:
        antPath = np.zeros((antNum, cityNum)).astype(int) - 1  # Путь муравья
        firstCity = [i for i in range(cityNum)]
        rd.shuffle(firstCity)  # Случайно назначьте начальный город для каждого муравья
        unvisted = []
        p = []
        pAccum = 0
        for i in range(cityNum):
            antPath[i][0] = firstCity[i]

        for i in range(len(antPath[0]) - 1):  # Постепенно обновляйте следующий город, в который собирается каждый муравей
            for j in range(len(antPath)):
                for k in range(cityNum):
                    if k not in antPath[j]:
                        unvisted.append(k)
                for m in unvisted:
                    pAccum += pheromone[antPath[j][i]][m] ** alpha * heuristic[antPath[j][i]][m] ** beta
                for n in unvisted:
                    p.append(pheromone[antPath[j][i]][n] ** alpha * heuristic[antPath[j][i]][n] ** beta / pAccum)

                roulette = np.array(p).cumsum()  # Создать рулетку
                r = rd.uniform(min(roulette), max(roulette))
                for x in range(len(roulette)):
                    if roulette[x] >= r:  # Используйте метод рулетки, чтобы выбрать следующий город
                        antPath[j][i + 1] = unvisted[x]
                        break
                unvisted = []
                p = []
                pAccum = 0
        pheromone = (1 - pheEvaRate) * pheromone  # Феромон летучий
        length = lengthCal(antPath, distance_matrix)
        for i in range(len(antPath)):
            for j in range(len(antPath[i]) - 1):
                pheromone[antPath[i][j]][antPath[i][j + 1]] += 1 / length[i]  # Обновление феромона
            pheromone[antPath[i][-1]][antPath[i][0]] += 1 / length[i]
        iter += 1
    return antPath


def enter(ant, iter):
    global antNum
    antNum = ant
    global itermax
    itermax = iter


def column(matrix, i):
    return [row[i] for row in matrix]


def findCorrectPath(arr):
    distance_matrix = cal_distance_matrix()

    a = len(distance_matrix) + 1
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * 3
    for i in range(len(distance_matrix)):
        for j in range(len(arr)):
            if i == j:
                mas[i][0] = arr[j]
                mas[i][1] = distance_matrix[i][0]
                mas[i][2] = distance_matrix[i][1]
    mas[10][0] = arr[0]
    mas[10][1] = distance_matrix[0][0]
    mas[10][2] = distance_matrix[0][1]

    return mas


if __name__ == '__main__':
    dis = cal_distance_matrix()
    # comAlgoritn = CommonAlg(120, 1, 3, 0.3, dis)
    # arr = comAlgoritn._commonAlgorithm()
    arr = alg(15, 1, 3, 0.3, cal_distance_matrix(), 100)
    mas = findCorrectPath(arr)

    best_x = column(mas, 1)
    best_y = column(mas, 2)

    plt.plot(best_x, best_y)
    plt.show()
