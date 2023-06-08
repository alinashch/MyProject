import numpy as np


class CommonAlg:  # класс алгоритма муравьиной колонии для решения задачи коммивояжёра
    def __init__(self, func, numCity, size_pop, max_iter, distance_matrix=None, alpha=1, beta=2, rho=0.1):
        self.func = func
        self.numCity = numCity
        self.size_pop = size_pop
        self.max_iter = max_iter
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.prob_matrix_distance = 1 / (distance_matrix + 1e-10 * np.eye(numCity, numCity))
        self.antPath = np.ones((numCity, numCity))
        self.Table = np.zeros((size_pop, numCity)).astype(int)
        self.y = None
        self.generation_best_X, self.generation_best_Y = [], []
        self.y_best_history = self.generation_best_Y
        self.best_x, self.best_y = None, None
        self.y_history_all=[]

    def run(self, max_iter=None):
        self.max_iter = max_iter or self.max_iter
        for i in range(self.max_iter):
            prob_matrix = (self.antPath ** self.alpha) * (self.prob_matrix_distance) ** self.beta
            for j in range(self.size_pop):
                self.Table[j, 0] = 0
                for k in range(self.numCity - 1):
                    taboo_set = set(self.Table[j, :k + 1])
                    allow_list = list(set(range(self.numCity)) - taboo_set)
                    prob = prob_matrix[self.Table[j, k], allow_list]
                    prob = prob / prob.sum()
                    next_point = np.random.choice(allow_list, size=1, p=prob)[0]
                    self.Table[j, k + 1] = next_point

            y = np.array([self.func(i) for i in self.Table])

            self.y_history_all.append(np.average(y))
            index_best = y.argmin()
            x_best, y_best = self.Table[index_best, :].copy(), y[index_best].copy()
            self.generation_best_X.append(x_best)
            self.generation_best_Y.append(y_best)
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
