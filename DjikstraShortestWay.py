import heapq

# Calculer le plus court chemain #

class Node:
    key = ""
    adjacents = {}
    distance = 20000000000
    visited = False
    previous = None

    def __init__(self, key):
        self.key = key
        self.adjacents = {}
        self.visited = False

    def reset(self):
        self.visited = False
        self.distance = 20000000000
        self.previous = None

    def add_branch(self, other, time):
        self.adjacents[other] = time

    def get_connections(self):
        return self.adjacent.keys()

    def get_time(self, other):
        return self.adjacents[other]

    def get_distance(self):
        return self.distance

    def set_distance(self, value):
        self.distance = value

    def get_key(self):
        return self.key

    def set_visited(self):
        self.visited = True

    def set_previous(self, prev):
        self.previous = prev

    def __lt__(self, other):
        return self.distance < other.distance

    def __cmp__(self, other):
        if self.distance < other.distance:
            return -1
        elif self.distance > other.distance:
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.key) + ' adjacent: ' + str([x.key for x in self.adjacents])

def create_graph(dataframe):
    graph = []
    for _, row in dataframe.iterrows():
        start = row["start"]
        destination = row["destination"]
        duree = row["duree"]

        # Vérification des doublons avant l'insertion
        if not any(x.key == start for x in graph):
            graph.append(Node(start))
        if not any(x.key == destination for x in graph):
            graph.append(Node(destination))

        # L'ajout des branches dans les deux sens
        start_node = next(x for x in graph if x.key == start)
        destination_node = next(x for x in graph if x.key == destination)
        start_node.add_branch(destination_node, duree)
        destination_node.add_branch(start_node, duree)
    return graph

def dij(graph, start, destination):

    # Définir la distance du noeud de depart
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisited_queue)
    while len(unvisited_queue):
        # Ouvrir un sommet avec la plus petite distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # Parcourir les adjacents
        for next in current.adjacents:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_time(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # Ajouter les sommets non visités
        unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)

def extract(nodes, city):
    res = []
    for x in nodes:
        if city in x.key:
            res.append(x)
    return res

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_key())
        shortest(v.previous, path)
