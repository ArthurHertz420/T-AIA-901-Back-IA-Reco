import copy

from DjikstraShortestWay import *


def find_path(dataframe, start, destination):
    # Creation du graph
    graph = create_graph(dataframe)
    start_capitalize = start.capitalize()
    destination_capitalize = destination.capitalize()
    start_cities = extract(graph, start_capitalize)
    destination_cities = extract(graph, destination_capitalize)

    res = None
    result = None
    for start_capitalize in start_cities:
        for destination_capitalize in destination_cities:

            for node in graph:
                node.reset()
            dij(graph, start_capitalize, destination_capitalize)

            target = destination_capitalize
            path = [target.get_key()]
            shortest(target, path)
            if res is not None and res.get_distance() < target.get_distance():
                res = copy.copy(target)
                result = copy.copy(path[::-1])
            else:
                res = copy.copy(target)
                result = copy.copy(path[::-1])
                print('Le plus court chemain est: %s' % (path[::-1]))
                return result
    return result
