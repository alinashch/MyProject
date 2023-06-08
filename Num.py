def initNumCity(numCity):
    a = numCity
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * numCity
    for j in range(len(mas)):
        for i in range(len(mas)):
            if i == j:
                mas[i][j] = 1
            else:
                mas[i][j] = 0
    return mas


def initNullMas(numCity):
    a = numCity
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * numCity
    for j in range(len(mas)):
        for i in range(len(mas)):
            mas[i][j] = 0
    return mas


def initOneMas(numCity):
    a = numCity
    mas = [0] * a
    for i in range(a):
        mas[i] = [0] * numCity
    for j in range(len(mas)):
        for i in range(len(mas)):
            mas[i][j] = 1
    return mas


def Min(generation_best_Y):
    temp = min(generation_best_Y)
    res = []
    for idx in range(0, len(generation_best_Y)):
        if temp == generation_best_Y[idx]:
            res.append(idx)
    return res


def AVG(generation_best_Y):
    sum_lst = sum(generation_best_Y)
    lst_avg = sum_lst / len(generation_best_Y)
    return lst_avg


def findPathFromCityNum(distance_matrix, table):
    res=[]
    for i in range(len(table) - 1):
        start = i
        finish = i + 1
        for j in range(len(distance_matrix)):
            for k in range(len(distance_matrix)):
                if j == start and k == finish:
                    res.append( distance_matrix[j][k])
