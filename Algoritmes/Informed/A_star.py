from Classes.Frontier import frontier

def a_star_search(problem, heuristic):
    initial_node = problem.initial_node
    initial_node.set_h_value(heuristic(initial_node))
    if problem.goal_test(initial_node) is True:
        return ('Succes', problem.solution(initial_node))  # solution kan bekomen worden uit parent nodes

    nodes_queue = frontier("gh")  # priority queue

    nodes_queue.add(initial_node)

    node_states_explored = []
    node_states_in_frontier = []
    node_states_in_frontier.append(initial_node.state)

    while True:
        if nodes_queue.is_empty():
            return ('Failure', None)

        current_node = nodes_queue.pop()  # pop of cost queue

        yield current_node

        if problem.goal_test(current_node) is True:
            return ('Succes', problem.solution(current_node))

        node_states_in_frontier.remove(current_node.state)
        node_states_explored.append(current_node.state)

        for action in problem.availableActions(current_node):
            child_node = problem.getChildFromAction(action, current_node)
            child_node.set_h_value(heuristic(child_node))
            if child_node.state not in node_states_explored and child_node.state not in node_states_in_frontier:
                nodes_queue.add(child_node)
                node_states_in_frontier.append(child_node.state)
            elif child_node.state in node_states_in_frontier:
                potential_replace(child_node, nodes_queue)

def potential_replace(new_node, frontier):
    for node in frontier.nodes:
        if new_node.state == node.state:
            if new_node.f_value < node.f_value:
                frontier.replace_node(new_node, node)
