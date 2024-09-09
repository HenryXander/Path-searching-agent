from Classes import Node


class search_problem():

    def __init__(self, initial_state, goal_state, transition_model):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.transition_model = transition_model
        self.initial_node = Node.Node(self, initial_state, None, None, 0, 0)


    def goal_test(self, node):
        node_state = node.state
        return node_state == self.goal_state

    def solution(self, node):
        solution_array = [node]
        current_state = node.state
        while current_state != self.initial_state:
            node = node.parent
            current_state = node.state
            solution_array.append(node)
        return solution_array

    def availableActions(self, node):
        return self.transition_model.get_actions(node)

    def getChildFromAction(self, action, node):
        child_node = node.get_child_node_from_action(action)
        return child_node

    def getNonDeterministicChildsFromAction(self, action, node):
        resulting_states = self.transition_model.non_deterministic_results(node.state, action)
        resulting_nodes = []
        path_cost = node.g_value + self.step_cost(node.state, action)
        for resulting_state in resulting_states:
            resulting_node = Node.Node(self, resulting_state, node, action, path_cost, node.depth + 1)
            resulting_nodes.append(resulting_node)
        return resulting_nodes


    def result(self, state, action): # of node ipv state
        return self.transition_model.result(state, action)

    def step_cost(self, state, action):
        return self.transition_model.step_cost(state, action)

