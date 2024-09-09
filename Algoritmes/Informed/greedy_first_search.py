from Classes import Frontier

def greedy_first_search(problem, heurstic):
    initial_node = problem.initial_node
    initial_node.set_h_value(heurstic(initial_node))
    if problem.goal_test(initial_node) is True:
        return ('Succes', problem.solution(initial_node))  # solution kan bekomen worden uit parent nodes

    nodes_queue = Frontier.frontier('h')

    nodes_queue.add(initial_node)

    node_states_explored = []
    node_states_in_queue = []
    node_states_in_queue.append(initial_node.state)

    inf_loop_counter = 0

    while True:
        if nodes_queue.is_empty():
            return ('Failure', None)
        current_node = nodes_queue.pop()
        yield current_node
        if problem.goal_test(current_node) is True:
            return ('Succes', problem.solution(current_node))
        node_states_in_queue.remove(current_node.state)
        node_states_explored.append(current_node.state)
        for action in problem.availableActions(current_node):
            child_node = problem.getChildFromAction(action, current_node)
            child_node.set_h_value(heurstic(child_node))
            if child_node.state not in node_states_explored and child_node.state not in node_states_in_queue:
                nodes_queue.add(child_node)
                node_states_in_queue.append(child_node.state)

        inf_loop_counter += 1
        if inf_loop_counter > 10000:
            return ('Failure: 10 000 nodes tried', None)
