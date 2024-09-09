import math

def iterative_deepening_a_star_search(problem, heuristic):
    initial_node = problem.initial_node
    initial_node.set_h_value(heuristic(initial_node))
    bound = initial_node.f_value

    while True:
        result = yield from depth_first_search_cutoff(problem, initial_node, bound, heuristic)
        if result[0] == "Succes":
            return result  # This should be the solution path
        elif result[0] == "Failure" and result[1] == math.inf:
            return ("Failure", bound)
        bound = result[1]

def depth_first_search_cutoff(problem, node, bound, heuristic):
    f = node.g_value + node.h_value
    if f > bound:
        return ("Failure", f)

    if problem.goal_test(node):
        return ("Succes", problem.solution(node))

    min_bound = math.inf
    for action in problem.availableActions(node):
        child = problem.getChildFromAction(action, node)
        child.set_h_value(heuristic(child))

        yield child

        try:
            result = yield from depth_first_search_cutoff(problem, child, bound, heuristic)

            if result[0] == "Succes":
                return result
            else:
                min_bound = min(min_bound, result[1])

        except StopIteration as end:
            result = end.value
            if result[0] == "Succes":
                return result
            else:
                min_bound = min(min_bound, result[1])

    return ("Failure", min_bound)
