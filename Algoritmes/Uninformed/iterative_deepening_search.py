def iterative_depth_limited_search(problem, limit):
    initial_node = problem.initial_node
    stack = [(initial_node, 0)]  # Stack holds tuples of (node, depth)
    explored = {}
    while stack:
        current_node, current_depth = stack.pop()
        if problem.goal_test(current_node):
            return ('Succes', problem.solution(current_node))
        if current_depth < limit:
            explored[current_node.state] = current_depth
            yield current_node  # Yield for visualization
            for action in problem.availableActions(current_node):
                child_node = problem.getChildFromAction(action, current_node)
                if (child_node.state not in explored) or (child_node.depth < explored[child_node.state]):
                    explored[child_node.state] = child_node.depth
                    stack.append((child_node, current_depth + 1))
    return ('Failure', None)

def iterative_deepening_search(problem, limit):
    depth = 0
    while depth <= limit:
        result = yield from iterative_depth_limited_search(problem, limit)
        if result[0] == "Succes":
            return result
        depth += 1
    return ('Failure', None)