import numpy as np


def _max_min(self):
    for step in range(self.steps):
        iteration_best_tour = None
        iteration_best_distance = float("inf")
        iteration_all_distance = []
        for ant in self.ants:
            ant.find_tour()
            iteration_all_distance.append(ant.distance)
            if ant.get_distance() < iteration_best_distance:
                iteration_best_tour = ant.tour
                iteration_best_distance = ant.distance
        if float(step + 1) / float(self.steps) <= 0.75:
            self._add_pheromone(iteration_best_tour, iteration_best_distance)
            max_pheromone = self.pheromone_deposit_weight / iteration_best_distance
        else:
            if iteration_best_distance < self.global_best_distance:
                self.global_best_tour = iteration_best_tour
                self.global_best_distance = iteration_best_distance
            self._add_pheromone(self.global_best_tour, self.global_best_distance)
            max_pheromone = self.pheromone_deposit_weight / self.global_best_distance
        min_pheromone = max_pheromone * self.min_scaling_factor

        self.y_history_all.append(np.average(iteration_all_distance))
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j].pheromone *= (1.0 - self.rho)
                if self.edges[i][j].pheromone > max_pheromone:
                    self.edges[i][j].pheromone = max_pheromone
                elif self.edges[i][j].pheromone < min_pheromone:
                    self.edges[i][j].pheromone = min_pheromone