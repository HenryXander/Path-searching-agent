
#--------------------------------------recursive--------------------------------------

def depth_limited_search(problem, limit):
    initial_node = problem.initial_node
    result = yield from __recursive_DLS(initial_node, limit, problem)
    if result[0] == "Succes":
        return result
    else:
        return ('Failure', None)

def __recursive_DLS(node, limit, problem):
    if problem.goal_test(node):
        return ('Succes', problem.solution(node))
    elif limit == 0:
        return ('Cutoff', None)
    else:
        cutoff_occurred = False
        for action in problem.availableActions(node):
            child_node = problem.getChildFromAction(action, node)

            # Yield the child node for visualization
            yield child_node

            try:
                result = yield from __recursive_DLS(child_node, limit - 1, problem)
                if result[0] == 'Succes':
                    return result
                elif result[0] == 'Cutoff':
                    cutoff_occurred = True
            except StopIteration as end:
                result = end.value
                if result[0] == "Succes":
                    return result
                elif result[0] == "Cutoff":
                    cutoff_occurred = True

        return ('Cutoff' if cutoff_occurred else 'Failure', None)


#--------------------------------------iterative--------------------------------------
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