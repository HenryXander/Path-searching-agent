from Algoritmes.Uninformed.breadth_first_search import breadth_first_search as bfs
from Algoritmes.Uninformed.uniform_cost_search import uniform_cost_search as ucs
from Algoritmes.Uninformed.depth_first_search import depth_first_search as dfs
from Algoritmes.Uninformed.depth_limited_search import depth_limited_search as dls
from Algoritmes.Uninformed.depth_limited_search import iterative_depth_limited_search as idls
from Algoritmes.Uninformed.iterative_deepening_search import iterative_deepening_search as ids

class agent():

    def __init__(self, problem):
        self.problem = problem

    def breadth_first_search(self):
        return bfs(self.problem)

    def uniform_cost_search(self):
        return ucs(self.problem)

    def depth_first_search(self):
        return dfs(self.problem)

    def iterative_depth_limited_search(self, limit):
        return idls(self.problem, limit)

    def depth_limited_search(self, limit):
        return dls(self.problem, limit)

    def iterative_deepening_search(self, limit):
        return ids(self.problem, limit)
