import math, copy

def get_lowest_cost_node(node_array):
    if not node_array:
        return None
    lowest_node = node_array[0]
    lowest_cost = lowest_node.f_value
    for node in node_array:
        if node.f_value < lowest_cost:
            lowest_node = node
            lowest_cost = node.f_value
    return lowest_node


def recursive_best_first_search(problem, heuristic):
    initial_node = problem.initial_node
    initial_node.set_h_value(heuristic(initial_node))
    return RBFS(problem, heuristic, initial_node, math.inf)



def RBFS(problem, heuristic, node, f_limit):
    yield node
    if problem.goal_test(node):
        return ('Succes', problem.solution(node))
    else:
        successors = []
        for action in problem.availableActions(node):
            child_node = problem.getChildFromAction(action, node)
            child_node.set_h_value(heuristic(child_node))
            successors.append(child_node)
        if not successors:
            return ('Failure', math.inf)
        while True:
            if not successors:
                return ('Failure', math.inf)
            else:
                lowest_cost_node = get_lowest_cost_node(successors)
                if lowest_cost_node.f_value > f_limit:
                    return ('Failure', lowest_cost_node.f_value)
                copy_successors = copy.copy(successors)
                copy_successors.remove(lowest_cost_node)
                second_lowest_cost_node = get_lowest_cost_node(copy_successors)
                try:
                    if second_lowest_cost_node is not None:
                        result = yield from RBFS(problem, heuristic,lowest_cost_node, min(f_limit, second_lowest_cost_node.f_value))
                    else:
                        result = yield from RBFS(problem, heuristic, lowest_cost_node, min(f_limit, math.inf))

                    if result[0] == "Succes":
                        return result
                    elif result[1] is not math.inf:
                        lowest_cost_node.set_f_value(result[1])

                except StopIteration as end:
                    result = end.value
                    if 'Failure' not in result[0]:
                        return result
                    elif result[1] is not math.inf:
                        lowest_cost_node.set_f_value(result[1])