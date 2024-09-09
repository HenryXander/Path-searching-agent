from Classes import Frontier


def uniform_cost_search(problem):
    initial_node = problem.initial_node
    if problem.goal_test(initial_node) is True:
        return ('Succes', problem.solution(initial_node))  # solution kan bekomen worden uit parent nodes

    frontier = Frontier.frontier("g")  # priority queue

    frontier.add(initial_node)

    node_states_explored = []
    node_states_in_frontier = []
    node_states_in_frontier.append(initial_node.state)

    while True:
        if frontier.is_empty():
            return ('Failure', None)

        current_node = frontier.pop()  # pop of cost queue

        yield current_node

        if problem.goal_test(current_node) is True:
            return ('Succes', problem.solution(current_node))

        node_states_in_frontier.remove(current_node.state)
        node_states_explored.append(current_node.state)

        for action in problem.availableActions(current_node):
            child_node = problem.getChildFromAction(action, current_node)

            if child_node.state not in node_states_explored and child_node.state not in node_states_in_frontier:
                frontier.add(child_node)
                node_states_in_frontier.append(child_node.state)
            elif child_node.state in node_states_in_frontier:
                potential_replace(child_node, frontier)


def potential_replace(new_node, frontier):
    for node in frontier.nodes:
        if new_node.state == node.state:
            if new_node.g_value < node.g_value:
                frontier.replace_node(new_node, node)