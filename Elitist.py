import numpy as np

def _elitist(self):
    for step in range(self.steps):
        iteration_all_distance = []
        for ant in self.ants:
            self._add_pheromone(ant.find_tour(), ant.get_distance())
            iteration_all_distance.append(ant.distance)
            if ant.distance < self.global_best_distance:
                self.global_best_tour = ant.tour
                self.global_best_distance = ant.distance
        self._add_pheromone(self.global_best_tour, self.global_best_distance, weight=self.elitist_weight)
        self.y_history_all.append(np.average(iteration_all_distance))
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j].pheromone *= (1.0 - self.rho)
