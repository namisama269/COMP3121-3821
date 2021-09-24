from graphs.directedgraph import DirectedGraph

class FlowNetwork(DirectedGraph):
    """
    Source and sink are vertices 0 and n-1
    """
    def __init__(self, nV):
        super().__init__(nV)
        self.flows = [[None]*nV for _ in range(nV)]

    def insertEdge(self, v1, v2, weight):
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

    def vertexDefn(self, vertex):
        if vertex == 0:
            return 's'
        if vertex == self.nV-1:
            return 't'
        return str(vertex)
    
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
                    print(f"edge from {self.vertexDefn(i)}-{self.vertexDefn(j)} with capacity {self.edges[i][j]} and flow = {self.flows[i][j]}/{self.edges[i][j]}")

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

    # TODO: read in FN from file
    def readFile(self, filename):
        pass


def residualFlow(F):
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
                RF.insertEdge(i, j, residualFlow)

    return RF

if __name__ == "__main__":
    n = 6 # number of nodes in network including source and sink
    s, t = 0, n-1
    F = FlowNetwork(n)

    # insert edges
    F.insertEdge(s,1,16)
    F.insertEdge(s,2,13)
    F.insertEdge(1,2,10)
    F.insertEdge(2,1,4)
    F.insertEdge(1,3,12)
    F.insertEdge(2,4,14)
    F.insertEdge(3,2,9)
    F.insertEdge(4,3,7)
    F.insertEdge(3,t,20)
    F.insertEdge(4,t,4)

    # set flows
    """
    F.setFlow(s,1,11)
    F.setFlow(s,2,12)
    F.setFlow(1,2,0)
    F.setFlow(2,1,1)
    F.setFlow(1,3,12)
    F.setFlow(2,4,11)
    F.setFlow(3,2,0)
    F.setFlow(4,3,7)
    F.setFlow(3,t,19)
    F.setFlow(4,t,4)
    """
    F.setFlow(s,1,4)
    F.setFlow(1,3,4)
    F.setFlow(3,2,4)
    F.setFlow(2,4,4)
    F.setFlow(4,t,4)

    F.printFlows()
    print()

    F2 = residualFlow(F)
    F2.printFlows()

    print()

    F2.setFlow(s,1,7)
    F2.setFlow(1,2,7)
    F2.setFlow(2,4,7)
    F2.setFlow(4,3,7)
    F2.setFlow(3,t,7)

    F3 = residualFlow(F2)
    F3.printFlows()
