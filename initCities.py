
def column(matrix, i):
    return [row[i] for row in matrix]


def read_all_lines(filename):
    with open(filename) as file:
        return file.readlines()
from scipy import spatial


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