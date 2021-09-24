
class DirectedGraph:
    """
    Undirected, weighted graph using adjacency matrix representation

    Number of vertices is fixed at initialisation
    """
    def __init__(self, nV):
        self.nV = nV
        self.nE = 0
        self.edges = [[None]*nV for _ in range(nV)]

    def getNumVertices(self):
        return self.nV

    def getNumEdges(self):
        return self.nE

    def getEdgeWeight(self, v1, v2):
        if self.edges[v1][v2] is None:
            raise ValueError("Edge not in graph")
        return self.edges[v1][v2]

    def setEdgeWeight(self, v1, v2, weight):
        if self.edges[v1][v2] is None:
            raise ValueError("Edge not in graph")
        self.edges[v1][v2] = weight

    def edgeExists(self, v1, v2):
        return self.edges[v1][v2] is not None

    def insertEdge(self, v1, v2, weight=0):
        if self.edges[v1][v2] is not None:
            raise ValueError("Edge already in graph")
        self.edges[v1][v2] = weight
        self.nE += 1
    
    def removeEdge(self, v1, v2):
        if self.edges[v1][v2] is None:
            raise ValueError("Edge not in graph")
        self.edges[v1][v2] = None
        self.nE -= 1

    def printGraph(self):
        print(f"Graph has {self.nV} vertices and {self.nE} edges")
        print()
        print("Edges: ")
        for i in range(self.nV):
            for j in range(self.nV):
                if self.edges[i][j] is not None:
                    print(f"edge from {i}-{j} with weight {self.edges[i][j]}")

    def copy(self):
        new = DirectedGraph(self.nV)
        new.nE = self.nE
        new.edges = [[None]*self.nV for _ in range(self.nV)]
        for i in range(self.nV):
            for j in range(self.nV):
                new.edges[i][j] = self.edges[i][j]
        return new

    # TODO: read in graph from file
    def readFile(self, filename):
        pass

if __name__ == "__main__":
    pass