import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt
import pylab


class Salesman:
    def __init__(self, distances, basePheromoneValue=0.200, alpha=1.0, beta=4.0, antsCount=10, iterationCount=500,
                 pheramoneConst=0.64, pathScale=200):
        self.distances = distances
        self.citiesCount = len(self.distances[0]) + 1
        self.basePheromoneValue = basePheromoneValue
        self.pheromoneMap = self.createPheromoneMap()

        # Выбор вершины муравьём
        # коэффициент феромонов
        self.alpha = alpha
        # коэффициент короткого пути
        self.beta = beta

        # количество муравьёв
        self.antsCount = antsCount

        self.iterationCount = iterationCount

        # количетво ферамонов остающихся после испарения
        self.pheramoneConst = pheramoneConst

        # во сколько раз уменьшен путь, для получения значений от 0 до 1 (примерно)
        self.pathScale = pathScale

    @staticmethod
    def getTestDistance():
        # расстояния между городами
        # первая строка от 0 города до всех остальных
        # вторая строка от 1 города до всех остальных, кроме 0, и т.д.
        return [[0.612, 0.301, 0.866, 0.563, 0.327, 0.245, 0.443, 0.327, 0.248],
                [0.552, 0.439, 0.749, 0.491, 0.334, 0.350, 0.352, 0.303],
                [0.282, 0.506, 0.823, 0.619, 0.282, 0.368, 0.420],
                [0.623, 0.347, 0.261, 0.844, 0.431, 0.286],
                [0.755, 0.428, 0.601, 0.651, 0.441],
                [0.976, 0.391, 0.658, 0.758],
                [0.302, 0.501, 1.010],
                [0.699, 0.368],
                [0.755]
                ]

    @staticmethod
    def getTestSimpleDistance():
        # расстояния между городами
        # первая строка от 0 города до всех остальных
        # вторая строка от 1 города до всех остальных, кроме 0, и т.д.
        return [[5/5, 5/6, 5/14, 5/15],
                [5/7, 5/10, 5/6],
                [5/8, 5/7],
                [5/9,],

                ]

    def getLineValue(self, graph, a, b):
        if a > b:
            a, b = b, a

        return graph[a][-(self.citiesCount - b)]

    def setLineValue(self, graph, a, b, v):
        if a > b:
            a, b = b, a
        graph[a][-(self.citiesCount - b)] = v

    # self.pathScale константа пути, необходима чтобы увеличить порядок значения расстояния
    def getPathDistance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            distance += self.pathScale / self.getLineValue(self.distances, path[i], path[i + 1])
        return distance

    @staticmethod
    def getRandomDistance():
        print()

    def createPheromoneMap(self):
        return [[self.basePheromoneValue for j in range(self.citiesCount - i - 1, 0, -1)] for i in
                range(self.citiesCount - 1)]

    def lostPheramones(self):
        for row in range(len(self.pheromoneMap)):
            for col in range(len(self.pheromoneMap[row])):
                self.pheromoneMap[row][col] *= self.pheramoneConst
                if self.pheromoneMap[row][col] < self.basePheromoneValue:
                    self.pheromoneMap[row][col] = self.basePheromoneValue

    def updatePheramones(self, path, pathLength):
        pheramoneValue = self.beta / pathLength
        for i in range(len(path) - 1):
            self.setLineValue(self.pheromoneMap, path[i], path[i + 1],
                              self.getLineValue(self.pheromoneMap, path[i], path[i + 1]) + pheramoneValue)

    def findShortest(self, render=True, animate=True):
        min = 1000000000000000000000000
        minRoute = []
        for i in range(self.iterationCount):
            paths = self.runAnts()
            self.lostPheramones()
            for path in paths:
                pathLength = self.getPathDistance(path)
                self.updatePheramones(path, pathLength)
                if pathLength < min:
                    minRoute = path
                    min = pathLength
                # elif pathLength == min and not any([i==path[::-1] for i in minRoutes]):
                #     minRoutes.append(path)

        return min, minRoute

    def findShortestAll(self):
        minDistance = 1000000000000000000000000
        paths = []
        l = list(itertools.permutations([i for i in range(1, self.citiesCount)]))
        # print(l)
        for r in l:
            r = list(r)
            r.insert(0, 0)
            r.append(0)
            # print(r)
            length = sum([self.pathScale / self.getLineValue(self.distances, r[i], r[i + 1]) for i in range(len(r) - 1)])
            if length == minDistance and not any([i==r[::-1] for i in paths]):
                paths.append(r)
            elif length < minDistance:
                paths = [r]
                minDistance = length
        return minDistance, paths

    def draw(self, routes):
        G = nx.DiGraph()
        plt.figure(figsize=(8, 8), dpi=80)
        for route in routes:
            for i in range(len(route)-1):
                G.add_edges_from([(str(route[i]),str(route[i+1]))],weight=int(self.pathScale/self.getLineValue(self.distances,route[i],route[i+1])))
        # for i in range(self.citiesCount-1):
        #     for j in range(len(self.distances[i])):
        #         G.add_edges_from(
        #     [(str(i), str(i+j+1))], weight=int(200/self.distances[i][j]))

        # val_map = {'A': 1.0,
        #            'D': 0.5714285714285714,
        #            'H': 0.0}
        #
        # values = [val_map.get(node, 0.25) for node in G.nodes()]

        # Specify the edges you want here
        red_edges = []
        # for i in range(len(route)-1):
        #     red_edges.append((str(route[i],str(route[i+1]))))
        # red_edges = [('0', '1'), ('1', '2')]
        edge_colours = ['black' if not edge in red_edges else 'red'
                        for edge in G.edges()]
        black_edges = [edge for edge in G.edges() if edge not in red_edges]

        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in G.edges(data=True)])
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                               node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False)
        nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False, )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

    def runAnts(self):
        def runAnt(start):
            def getProb(a, b):
                return self.getLineValue(self.pheromoneMap, a, b) ** self.alpha * self.getLineValue(self.distances, a,
                                                                                                    b) ** self.beta

            def getNextCityIndex():
                r = random.random()
                for i in range(len(probNextCities)):
                    if r >= probNextCities[i]:
                        r -= probNextCities[i]
                    else:
                        return i

            # distance = 0
            route = [start]
            cities = list(range(self.citiesCount))
            cities.remove(start)

            while (cities):
                nextCitiesValues = [getProb(route[-1], newcity) for newcity in cities]
                # if not sum(nextCitiesValues):
                #     return True
                probNextCities = [prob / sum(nextCitiesValues) for prob in nextCitiesValues]
                newcity = cities[getNextCityIndex()]
                route.append(newcity)
                cities.remove(newcity)
            route.append(route[0])
            return route

        results = []
        for i in range(self.antsCount):
            results.append(runAnt(random.randint(0, self.citiesCount - 1)))
        return results
