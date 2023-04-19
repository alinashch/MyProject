import numpy as np
from scipy import spatial
import time
import matplotlib.pyplot as plt
import pandas as pd

from CommonAlg import CommonAlg
from UpgradeAlg import UpgradeAlg


def column(matrix, i):
    return [row[i] for row in matrix]


def read_all_lines(filename):
    with open(filename) as file:
        return file.readlines()


def enterFile():
    result = []
    lines = read_all_lines("city.txt")
    for line in lines:
        result.append(list(map(lambda x: float(x) * 100, line.split())))
    return result


def num_points():
    return len(enterFile())


def cal_distance_matrix():
    distance_matrix = spatial.distance.cdist(enterFile(), enterFile(), metric='euclidean')
    return  distance_matrix


def cal_total_distance(routine):
    num_points, = routine.shape
    return sum(
        [cal_distance_matrix()[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


def findCorrectPath(arr):
    a = len(cal_distance_matrix()) + 1
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * 3
    for i in range(len(cal_distance_matrix())):
        for j in range(len(arr)):
            if i == j:
                mas[i][0] = arr[j]
                mas[i][1] = cal_distance_matrix()[i][0]
                mas[i][2] = cal_distance_matrix()[i][1]
    mas[num_points()][0] = arr[0]
    mas[num_points()][1] = cal_distance_matrix()[0][0]
    mas[num_points()][2] = cal_distance_matrix()[0][1]

    return mas


def mainCom():
    distance_matrix=cal_distance_matrix()

    alg = CommonAlg(func=cal_total_distance, numCity=num_points(), size_pop=100, max_iter=100,
                    distance_matrix=distance_matrix)
    best_x, best_y = alg.run()

    fig, ax = plt.subplots(1, 2)
    best_points_ = np.concatenate([best_x, [best_x[0]]])
    best_points_coordinate = findCorrectPath(best_points_)
    best_x = column(best_points_coordinate, 1)
    best_y = column(best_points_coordinate, 2)
    for index in range(0, len(best_points_)):
        ax[0].annotate(best_points_[index], (best_x[index], best_y[index]))

    ax[0].plot(best_x, best_y, 'o-r')
    pd.DataFrame(alg.y_best_history).cummin().plot(ax=ax[1])
    plt.rcParams['figure.figsize'] = [20, 10]

    plt.show()

def mainUpg():
    distance_matrix=cal_distance_matrix()

    alg = UpgradeAlg(func=cal_total_distance, numCity=num_points(), size_pop=100, max_iter=100,
                    distance_matrix=distance_matrix)
    best_x, best_y = alg.run()

    fig, ax = plt.subplots(1, 2)
    best_points_ = np.concatenate([best_x, [best_x[0]]])
    best_points_coordinate = findCorrectPath(best_points_)
    best_x = column(best_points_coordinate, 1)
    best_y = column(best_points_coordinate, 2)
    for index in range(0, len(best_points_)):
        ax[0].annotate(best_points_[index], (best_x[index], best_y[index]))

    ax[0].plot(best_x, best_y, 'o-r')
    pd.DataFrame(alg.y_best_history).cummin().plot(ax=ax[1])
    plt.rcParams['figure.figsize'] = [20, 10]

    plt.show()


if __name__ == "__main__":
    mainCom()
    mainUpg()
