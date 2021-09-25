from graphs.directedgraph import DirectedGraph

class FlowNetwork(DirectedGraph):
    """
    Source and sink are vertices 0 and n-1
    """
    def __init__(self, nV):
        super().__init__(nV)
        self.flows = [[None]*nV for _ in range(nV)]

    def insertEdge(self, v1, v2, weight, residual=False):
        """
        If the network is not a residual, not allowed to insert edges from sink or to source
        Self loops are also not allowed to be inserted
        """
        if v1 == v2:
            raise ValueError("Cannot insert self-loop in flow network")
        if (v1 == self.nV-1 or v2 == 0) and not residual:
            raise ValueError("Cannot insert edge from sink or to source")
        super().insertEdge(v1, v2, weight)
        self.flows[v1][v2] = 0

    def removeEdge(self, v1, v2, weight):
         super().removeEdge(v1, v2, weight)
         self.flows[v1][v2] = None

    def setFlow(self, v1, v2, flow):
        if not self.edgeExists(v1, v2):
            raise ValueError("Edge not in graph, cannot set flow")
        if flow < 0:
            raise ValueError("Flow cannot be negative")
        self.flows[v1][v2] = flow

    def getFlow(self, v1, v2):
        if not self.edgeExists(v1, v2):
            return None
        return self.flows[v1][v2] 

    def getCapacity(self, v1, v2):
        return super().getEdgeWeight(v1, v2)

    def vertexIdxToName(self, vertex):
        if vertex == 0:
            return 's'
        if vertex == self.nV-1:
            return 't'
        return str(vertex)

    def vertexNameToIdx(self, name):
        if name == 's':
            return 0
        if name == 't':
            return self.nV-1
        return int(name)
    
    def isFlowEmpty(self):
        for i in range(self.nV):
            for j in range(self.nV):
                if self.flows[i][j] not in (None, 0):
                    return False
        return True
    
    def emptyFlows(self):
        for i in range(self.nV):
            for j in range(self.nV):
                if self.flows[i][j] is not None:
                    self.flows[i][j] = 0

    def printFlows(self):
        print(f"Graph has {self.nV} vertices and {self.nE} edges")
        print()
        print("Edges: ")
        for i in range(self.nV):
            for j in range(self.nV):
                if self.edges[i][j] is not None:
                    print(f"edge from {self.vertexIdxToName(i)}-{self.vertexIdxToName(j)} with capacity {self.edges[i][j]} and flow = {self.flows[i][j]}/{self.edges[i][j]}")

    def copy(self):
        new = FlowNetwork(self.nV)
        new.nE = self.nE
        new.edges = [[None]*self.nV for _ in range(self.nV)]
        new.flows = [[None]*self.nV for _ in range(self.nV)]
        for i in range(self.nV):
            for j in range(self.nV):
                new.edges[i][j] = self.edges[i][j]
                new.flows[i][j] = self.flows[i][j]
        return new

    def importFromGraph(self, G):
        """
        Create directed graph by importing from existing undirected graph
        """
        self.nV = G.nV
        self.nE = G.nE
        self.edges = [[None]*G.nV for _ in range(G.nV)]
        self.flows = [[None]*G.nV for _ in range(G.nV)]
        for i in range(G.nV):
            for j in range(G.nV):
                self.edges[i][j] = G.edges[i][j]
                if G.edges[i][j] is not None:
                    self.flows[i][j] = 0

def importFNFromFile(filename):
    """
    Import flow network from file, no error checks. Format:

    nV (number of vertices excluding )
    v1 v2 capacity flow
    ...

    (integer) capacity of the edge (edge weight) must be given
    flow = 0 if not given

    Return the FlowNetwork object.
    """
    f = open(filename, 'r')
    lines = f.readlines()
    nV = int(lines[0]) + 2
    F = FlowNetwork(nV)
    for i, line in enumerate(lines):
        if i == 0:
            continue
        line = line.split()
        v1, v2, cap = F.vertexNameToIdx(line[0]), F.vertexNameToIdx(line[1]), int(line[2])
        flow = 0 if len(line) < 4 else float(line[3])
        F.insertEdge(v1, v2, cap)
        F.setFlow(v1, v2, flow)
    f.close()

    return F

def residualFlow(F):
    """
    Return the residual flow network.
    """
    nV = F.nV
    RF = FlowNetwork(nV)
    
    for i in range(nV):
        for j in range(nV):
            if not (F.edgeExists(i, j) or F.edgeExists(j, i)):
                continue
            forwardFlow = F.getFlow(i, j) if F.edgeExists(i, j) else 0
            backwardFlow = F.getFlow(j, i) if F.edgeExists(j, i) else 0
            capacity = F.getEdgeWeight(i, j) if F.edgeExists(i, j) else 0
            residualFlow = capacity - forwardFlow + backwardFlow
            if residualFlow > 0:
                RF.insertEdge(i, j, residualFlow, residual=True)

    return RF

if __name__ == "__main__":
    pass