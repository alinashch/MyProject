import numpy as np
from scipy.stats import entropy


class UpgradeAlg:  # класс алгоритма муравьиной колонии для решения задачи коммивояжёра
    def __init__(self, func, numCity, size_pop, max_iter, distance_matrix=None, alpha=1, beta=2, rho=0.1):
        self.func = func
        self.numCity = numCity  # количество городов
        self.size_pop = size_pop  # количество муравьёв
        self.max_iter = max_iter  # количество итераций
        self.alpha = alpha  # коэффициент важности феромонов в выборе пути
        self.beta = beta  # коэффициент значимости расстояния
        self.rho = rho  # скорость испарения феромонов

        self.prob_matrix_distance = 1 / (distance_matrix + np.eye(numCity, numCity))

        self.antPath = np.ones((numCity, numCity))
        self.Table = np.zeros((size_pop, numCity)).astype(int)
        self.y = None
        self.generation_best_X, self.generation_best_Y = [], []
        self.x_best_history, self.y_best_history = self.generation_best_X, self.generation_best_Y
        self.best_x, self.best_y = None, None
        self.y_history_all=[]


    def run(self, max_iter=None):
        self.max_iter = max_iter or self.max_iter
        Emax = 0
        for i in range(len(self.prob_matrix_distance[0])):
            for k in range(len(self.prob_matrix_distance)):
                if self.prob_matrix_distance[i][k] != 0:
                    Emax += entropy(self.prob_matrix_distance[i], base=10)
        for i in range(self.max_iter):
            Ecurr = 0
            prob_matrix = (self.antPath ** self.alpha) * (self.prob_matrix_distance) ** self.beta
            for j in range(self.size_pop):
                self.Table[j, 0] = 0
                for k in range(self.numCity - 1):
                    taboo_set = set(self.Table[j, :k + 1])
                    allow_list = list(set(range(self.numCity)) - taboo_set)
                    prob = prob_matrix[self.Table[j, k], allow_list]
                    Ecurr += entropy(prob, base=10)
                    prob = prob / prob.sum()
                    next_point = np.random.choice(allow_list, size=1, p=prob)[0]
                    self.Table[j, k + 1] = next_point

            E = 1 - (Emax - Ecurr) / Emax
            if E > 0.86:
                self.beta = 5
            elif 0.55 <= E < 0.85:
                self.beta = 4
            elif 0.10 <= E < 0.55:
                self.beta = 3
            elif E < 0.10:
                self.beta = 2

            y = np.array([self.func(i) for i in self.Table])

            index_best = y.argmin()
            x_best, y_best = self.Table[index_best, :].copy(), y[index_best].copy()
            self.generation_best_X.append(x_best)
            self.generation_best_Y.append(y_best)
            self.y_history_all.append(np.average(y))


            delta_tau = np.zeros((self.numCity, self.numCity))
            for j in range(self.size_pop):
                for k in range(self.numCity - 1):
                    n1, n2 = self.Table[j, k], self.Table[j, k + 1]
                    delta_tau[n1, n2] += 1 / y[j]

                n1, n2 = self.Table[j, self.numCity - 1], self.Table[j, 0]
                delta_tau[n1, n2] += 1 / y[j]

            self.antPath = (1 - self.rho) * self.antPath + delta_tau

        best_generation = np.array(self.generation_best_Y).argmin()
        self.best_x = self.generation_best_X[best_generation]
        self.best_y = self.generation_best_Y[best_generation]
        return self.best_x, self.best_y

    fit = run