import numpy as np
from matplotlib import animation
from ply.cpp import xrange
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
    lines = read_all_lines("city2.txt")
    for line in lines:
        result.append(list(map(lambda x: float(x), line.split())))
    return result


def num_point(enterFile):
    return len(enterFile)


def cal_distance_matrix(enterFile):
    distance_matrix = spatial.distance.cdist(enterFile, enterFile, metric='euclidean')
    return distance_matrix


def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([cal_distance_matrix(enterFile())[routine[i % num_points], routine[(i + 1) % num_points]] for i in
                range(num_points)])


def Moving_Avg(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


def findCorrectPath(arr):
    a = len(enterFile()) + 1
    mas = [0] * a
    k = 0
    for i in range(a):
        mas[i] = [0] * 3
    for j in range(len(arr)):
        for i in range(len(enterFile())):
            if i == arr[j]:
                mas[k][0] = arr[j]
                mas[k][1] = enterFile()[arr[j]][0]
                mas[k][2] = enterFile()[arr[j]][1]
                k += 1
                break

    mas[num_point(enterFile())][0] = arr[0]
    mas[num_point(enterFile())][1] = enterFile()[0][0]
    mas[num_point(enterFile())][2] = enterFile()[0][1]

    return mas


def mainCom():
    distance_matrix = cal_distance_matrix(enterFile())
    alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=200,
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
    print(pd.DataFrame(alg.y_best_history).cummin())
    print(alg.y_history_all)
    plt.rcParams['figure.figsize'] = [20, 10]

    plt.show()


def mainUpg():
    distance_matrix = cal_distance_matrix(enterFile())
    alg = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=100, max_iter=200,
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
    print(pd.DataFrame(alg.y_best_history).cummin())
    print(alg.y_history_all)

    plt.show()


def mainUpgGraphAVGSpeedStudyRep():
    distance_matrix = cal_distance_matrix(enterFile())
    resUpd = []
    arr = []
    for i in range(49):
        arr.append(i)

    alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                      distance_matrix=distance_matrix)
    alg2.run()

    resUpd.append(Moving_Avg(alg2.y_history_all, 2))
    for i in range(len(resUpd)):
        plt.plot(arr, resUpd[i], color='b')

    plt.show()


def Disp():
    distance_matrix = cal_distance_matrix(enterFile())
    resCom = []
    resUpd = []
    arr = []
    p = 2
    fig, ax = plt.subplots(1, 2)

    for i in range(49):
        arr.append(i)

    for i in range(p):
        print(i)
        alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                        distance_matrix=distance_matrix)
        alg.run()

        alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                          distance_matrix=distance_matrix)
        alg2.run()

        resCom.append(Moving_Avg(alg.y_history_all, 2))
        resUpd.append(Moving_Avg(alg2.y_history_all, 2))
    resOneCom = []
    resOneUpd = []
    dotCom = []
    dotUpg = []
    for i in range(49):
        k = column(resCom, i)
        m = column(resUpd, i)
        K = sum(k)
        M = sum(m)
        dotCom.append(k)
        dotUpg.append(m)
        resOneCom.append(K / p)
        resOneUpd.append(M / p)


    disCom = []
    disUpg = []
    for i in range(len(dotCom)):
        for j in range(len(dotCom[0])):
            disCom.append(abs(dotCom[i][j] - resOneCom[i]))
            disUpg.append(abs(dotUpg[i][j] - resOneUpd[i]))

    ax[0].plot(arr, resOneCom, color='g')
    ax[0].plot(arr, resOneUpd, color='b')

    ax[1].plot( disCom, color='g')
    ax[1].plot( disUpg, color='b')

    plt.show()


def mainComGraphAVGSpeedStudyRepOneLine():
    distance_matrix = cal_distance_matrix(enterFile())
    resCom = []
    resUpd = []
    arr = []
    p = 10
    for i in range(9):
        arr.append(i)

    for i in range(p):
        alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                        distance_matrix=distance_matrix)
        alg.run()

        alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                          distance_matrix=distance_matrix)
        alg2.run()

        resCom.append(Moving_Avg(alg.y_history_all, 2))
        resUpd.append(Moving_Avg(alg2.y_history_all, 2))
    resOneCom = []
    resOneUpd = []

    for i in range(49):
        k = column(resCom, i)
        m = column(resUpd, i)
        K = sum(k)
        M = sum(m)
        resOneCom.append(K / p)
        resOneUpd.append(M / p)

    plt.plot(resOneCom, color='g')
    plt.plot(resOneUpd, color='b')
    plt.show()


def mainComGraphAVGSpeedStudyRep():
    distance_matrix = cal_distance_matrix(enterFile())
    resCom = []
    resUpd = []
    arr = []
    for i in range(49):
        arr.append(i)

    for i in range(2):
        print(i)
        alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                        distance_matrix=distance_matrix)
        alg.run()

        alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                          distance_matrix=distance_matrix)
        alg2.run()

        resCom.append(Moving_Avg(alg.y_history_all, 2))
        resUpd.append(Moving_Avg(alg2.y_history_all, 2))

    for i in range(len(resCom)):
        plt.plot(arr, resCom[i], color='g')
        plt.plot(arr, resUpd[i], color='b')

    plt.show()


def mainComGraphAVGSpeedStudy():
    distance_matrix = cal_distance_matrix(enterFile())
    alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                    distance_matrix=distance_matrix)
    alg.run()

    alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=50, max_iter=50,
                      distance_matrix=distance_matrix)
    alg2.run()

    datasetCom = alg.y_history_all
    resultCom = Moving_Avg(datasetCom, 2)
    plt.plot(alg.y_history_all, 'o', color='g')
    plt.plot(resultCom, color='g')

    plt.plot(alg2.y_history_all, 'o', color='b')
    plt.plot(Moving_Avg(alg2.y_history_all, 2), color='b')

    plt.show()


def mainComGraphMINSpeedStudy():
    distance_matrix = cal_distance_matrix(enterFile())
    alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=100, max_iter=100,
                    distance_matrix=distance_matrix)
    alg.run()
    alg2 = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=100, max_iter=100,
                      distance_matrix=distance_matrix)
    alg2.run()
    x = min(alg.generation_best_Y)
    plt.axhline(x, color='g')
    plt.plot(alg.generation_best_Y, 'o', color='g')

    y = min(alg2.generation_best_Y)
    plt.axhline(y, color='b')
    plt.plot(alg2.generation_best_Y, 'o', color='b')

    plt.show()


def CommonRep():
    distance_matrix = cal_distance_matrix(enterFile())
    for i in range(20):
        alg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=10, max_iter=10,
                        distance_matrix=distance_matrix)
        alg.run()

        x = alg.y_best_history
        print(i)
        print(alg.y_best_history)
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
        plt.plot(q)
    plt.show()


def UpgRep():
    distance_matrix = cal_distance_matrix(enterFile())
    for i in range(20):
        alg = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=10, max_iter=10,
                         distance_matrix=distance_matrix)
        alg.run()

        x = alg.y_best_history
        print(i)
        print(alg.y_best_history)
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
        plt.plot(q)
    plt.show()


def UpgAvg():
    res = []
    distance_matrix = cal_distance_matrix(enterFile())
    for i in range(20):
        alg = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=20, max_iter=20,
                         distance_matrix=distance_matrix)
        alg.run()
        x = alg.y_best_history
        print(i)
        print(alg.y_best_history)
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
            qq = np.average(q)
        print(qq)
        res.append(qq)
    plt.plot(res)
    plt.axhline(np.nanmean(res), color='g')

    plt.show()


def ComAAvg():
    res = []
    distance_matrix = cal_distance_matrix(enterFile())
    for i in range(20):
        alg = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=20, max_iter=20,
                         distance_matrix=distance_matrix)
        alg.run()
        x = alg.y_best_history
        print(i)
        print(alg.y_best_history)
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
            qq = np.average(q)
        print(qq)
        res.append(qq)
    plt.plot(res)
    plt.axhline(np.nanmean(res), color='g')
    plt.show()


def AllAvg():
    Cres = []
    Ures = []
    distance_matrix = cal_distance_matrix(enterFile())
    for i in range(30):
        Ualg = UpgradeAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=30, max_iter=30,
                          distance_matrix=distance_matrix)
        Ualg.run()

        Calg = CommonAlg(func=cal_total_distance, numCity=num_point(enterFile()), size_pop=30, max_iter=30,
                         distance_matrix=distance_matrix)
        Calg.run()
        x = Ualg.y_best_history
        xc = Calg.y_best_history
        print(i)
        print(Ualg.y_best_history)
        df = pd.DataFrame(x).cummin()
        dfc = pd.DataFrame(xc).cummin()
        q = []
        for i in range(len(df)):
            q.append(df[0].loc[i])
            qq = np.average(q)
        print(qq)
        Ures.append(qq)

        q = []
        for i in range(len(dfc)):
            q.append(dfc[0].loc[i])
            qq = np.average(q)
        print(qq)
        Cres.append(qq)

    plt.plot(Ures, color='g')
    plt.axhline(np.nanmean(Ures), color='r')

    plt.plot(Cres, color='b')
    plt.axhline(np.nanmean(Cres), color='y')
    plt.show()
    '''
if __name__ == "__main__":
    mainCom()
    mainUpg()
    
if __name__ == "__main__":
    CommonRep()
    UpgRep()
    '''


if __name__ == "__main__":
    mainCom()
    mainUpg()
