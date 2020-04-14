def earliest_ancestor(ancestors, starting_node):
    parents = get_parents(ancestors, starting_node)
    if len(parents) == 0:
        return -1

    deepest_path = []
    for par in parents:
        path = earliest_ancestor_util(ancestors, par, [starting_node])
        # print(f"PATH: {path}")
        if len(path) > len(deepest_path):
            deepest_path = path
        else:
            if len(path) == len(deepest_path):
                # Same length, choose smallest id
                if path[-1] < deepest_path[-1]:
                    deepest_path = path

    return deepest_path[-1]


def earliest_ancestor_util(ancestors, node, path):
    parents = get_parents(ancestors, node)
    path.append(node)

    if len(parents) == 0:
        return path

    deepest_path = []

    for p in parents:
        new_path = list(path)
        found_path = earliest_ancestor_util(ancestors, p, new_path)
        if len(found_path) > len(deepest_path):
            deepest_path = found_path

    return deepest_path


def get_parents(ancestor_list, child_node):
    parents = []
    for pair in ancestor_list:
        if pair[1] == child_node:
            parents.append(pair[0])

    return parents
