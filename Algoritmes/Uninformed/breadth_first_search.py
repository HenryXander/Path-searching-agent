import queue

def breadth_first_search(problem):
    initial_node = problem.initial_node
    if problem.goal_test(initial_node) is True:
        return ('Succes', problem.solution(initial_node))  # solution kan bekomen worden uit parent nodes

    nodes_queue = queue.Queue()  # FIFO queue
    nodes_queue.put(initial_node)
    node_states_explored = []
    node_states_in_queue = []
    node_states_in_queue.append(initial_node.state)

    while True:
        if nodes_queue.empty():
            return ('Failure', None)

        current_node = nodes_queue.get()  # pop of FIFO queue

        yield current_node

        node_states_in_queue.remove(current_node.state)
        node_states_explored.append(current_node.state)

        for action in problem.availableActions(current_node):
            child_node = problem.getChildFromAction(action, current_node)

            if child_node.state not in node_states_explored and child_node.state not in node_states_in_queue:
                if problem.goal_test(child_node) is True:
                    return ('Succes', problem.solution(child_node))
                nodes_queue.put(child_node)
                node_states_in_queue.append(child_node.state)