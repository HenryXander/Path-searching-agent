from Algoritmes.Informed.greedy_first_search import greedy_first_search as gfs
from Algoritmes.Informed.recursive_best_first_search import recursive_best_first_search as rbfs
from Algoritmes.Informed.A_star import a_star_search as Astar
from Algoritmes.Informed.Iterative_deepening_A_star import iterative_deepening_a_star_search as IDA_star
from Algoritmes.Informed.Simplified_memory_bounded_A_star import simplified_memory_bounded_a_star_search as SMA_star

class agent():

    def __init__(self, problem, heuristic):
        self.problem = problem
        self.heuristic = heuristic

    def greedy_first_search(self):
        return gfs(self.problem, self.heuristic)

    def recursive_best_first_search(self):
        return rbfs(self.problem, self.heuristic)

    def a_star_search(self):
        return Astar(self.problem, self.heuristic)

    def iterative_deepening_a_star_search(self):
        return IDA_star(self.problem, self.heuristic)

    def simplified_memory_bounded_a_star(self, memory_limit):
        return SMA_star(self.problem, self.heuristic, memory_limit)
