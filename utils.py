def load_to_list(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def traverse_nested_list(l, depth=0, id=0):
    if l == []:
        yield [-1, depth, id]
    if isinstance(l, list):
        for id, i in enumerate(l):
            yield from traverse_nested_list(i, depth+1, id)
    else:
        yield [l, depth, id]