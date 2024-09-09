from Classes.Frontier import frontier
import math

def simplified_memory_bounded_a_star_search(problem, heuristic, memory_limit):
    initial_node = problem.initial_node
    initial_node.set_h_value(heuristic(initial_node))
    if problem.goal_test(initial_node) is True:
        return ('Succes', problem.solution(initial_node))  # solution kan bekomen worden uit parent nodes

    nodes_queue = frontier("gh")  # priority queue

    nodes_queue.add(initial_node)

    node_states_explored = []
    node_states_in_frontier = {initial_node.state : initial_node}

    while True:
        if nodes_queue.is_empty():
            return ('Failure', None)

        current_node = nodes_queue.pop()  # pop of cost queue

        yield current_node

        if problem.goal_test(current_node) is True:
            return ('Succes', problem.solution(current_node))

        node_states_in_frontier.pop(current_node.state, None)
        node_states_explored.append(current_node.state)

        successors = []
        for action in problem.availableActions(current_node):
            child_node = problem.getChildFromAction(action, current_node)
            child_node.set_h_value(heuristic(child_node))
            if child_node.state not in node_states_explored and child_node.state not in node_states_in_frontier:
                successors.append(child_node)
            elif child_node.state in node_states_in_frontier:
                potential_replace(child_node, nodes_queue)

        for child_node in successors:
            if nodes_queue.size() >= memory_limit:
                prune_least_promising(nodes_queue, node_states_in_frontier)
            nodes_queue.add(child_node)
            node_states_in_frontier[child_node.state] = child_node

        if current_node.depth > memory_limit:
            current_node.set_f_value(math.inf)

def potential_replace(new_node, frontier):
    for node in frontier.nodes:
        if new_node.state == node.state:
            if new_node.f_value < node.f_value:
                frontier.replace_node(new_node, node)

def prune_least_promising(frontier, node_states_in_frontier):
    # Remove the node with the highest f-value from the frontier
    least_promising_node = max(frontier.nodes, key=lambda n: n.f_value)
    frontier.remove_node(least_promising_node)
    node_states_in_frontier.pop(least_promising_node.state, None)