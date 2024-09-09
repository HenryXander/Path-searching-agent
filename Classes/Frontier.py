class MemoryFrontierFull(Exception):
    pass

class frontier():

    def __init__(self, relevant_cost, memory_size = None):      #relevant_cost = 'g' -> f(n) = g(n)
                                                                # relevant_cost = 'h' -> f(n) = h(n)
                                                                # relevant_cost = 'gh' -> f(n) = g(n) + h(n)
        self.relevant_cost = relevant_cost
        self.nodes = []
        self.memory_size = memory_size


    def size(self):
        return len(self.nodes)

    def add(self, node):
        if self.memory_size is not None and len(self.nodes) >= self.memory_size:
            raise MemoryFrontierFull("Can't add node in frontier. Memory of frontier is full")
        else:
            self.nodes.append(node)
            self.__sort_frontier()

    def pop(self):
        pop_node = self.nodes[0]
        self.nodes = self.nodes[1:]
        return pop_node

    def is_empty(self):
        return self.nodes == []

    def iter(self):
        return self.nodes

    def set_memory_size(self, memory_size):
        self.memory_size = memory_size

    def memory_full(self):
        return len(self.nodes) == self.memory_size

    def get_worst(self):
        return self.nodes[:-1]

    def remove_node(self, node_to_remove):
        self.nodes = [node for node in self.nodes if node != node_to_remove]

    def clear(self):
        self.nodes = []

    def get_k_best_successors(self, k):
        return self.nodes[:k]

    def __sort_frontier(self):
        for i in range(0, len(self.nodes), 1):
            for j in range(0, len(self.nodes) - i - 1, 1):
                node_relevant_cost = self.nodes[j].get_value(self.relevant_cost)  # Geef aan node class mee welke relevante cost in dit geval relevant is
                next_node_relevant_cost = self.nodes[j + 1].get_value(self.relevant_cost)
                if node_relevant_cost > next_node_relevant_cost:
                    temp = self.nodes[j]
                    self.nodes[j] = self.nodes[j + 1]
                    self.nodes[j + 1] = temp

    def Sort(self):
        self.__sort_frontier()


    def replace_node(self, new_node, old_node):
        self.nodes.remove(old_node)
        self.nodes.append(new_node)
        self.__sort_frontier()

