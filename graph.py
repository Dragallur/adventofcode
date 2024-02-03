def a_star(start, goal, h, neighbors):
    """
    A* algorithm for finding the shortest path from 'start' to 'goal' in a graph.
    'h' is the approximation of the distance from current position to the 'goal'.
    'neighbors' is a function that returns an iterable with possible neighbors 
    from the current position.
    """
    open_set = set([start])
    previous = {}
    g = {start: 0}

    f = {start: h(start, goal)}

    while open_set:
        current = min(open_set, key=lambda x: f[x])
        if current == goal:
            path = [current]
            while current in previous:
                current = previous[current]
                path.append(current)
            return path[::-1]

        open_set.remove(current)
        for neighbor in neighbors(current):
            t = g[current] + 1
            if neighbor in g and t >= g[neighbor]:
                continue
            g[neighbor] = t
            previous[neighbor] = current
            f[neighbor] = g[neighbor] + h(neighbor, goal)
            if neighbor not in open_set:
                open_set.add(neighbor)