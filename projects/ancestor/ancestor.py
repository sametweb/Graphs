def earliest_ancestor(ancestors, starting_node):
    tree = {}
    for p, c in ancestors:
        if c not in tree:
            tree[c] = [p]
        else:
            tree[c] += [p]

    if tree[starting_node] == []:
        return -1

    current_parents = tree[starting_node]
    for p in tree[starting_node]:
            if tree[p] != []:
                current_parents = tree[p]

    return current_parents


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))