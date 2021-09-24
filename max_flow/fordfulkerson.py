"""
Implementation of Ford-Fulkerson algorithm for finding max flow
"""
from graphs.graphtraversals import dfs
from flownetwork import FlowNetwork, residualFlow

def fordFulkerson(F):
    nV = F.getNumVertices()
    s, t = 0, nV-1
    maxFlow = 0
    
    # RF = computed residual flow networks (initially is the original network with no flow)
    # FW = original flow network with added flow
    RF = F
    FW = F.copy()

    while True:
        path = dfs(RF, s, t)
        if path is None:
            break

        """
        print('*'*70)
        print(f"Iteration {itt}")
        print('*'*70)
        print()
        print("F")
        F.printFlows()
        print()
        print("RF")
        RF.printFlows()
        print()

        print(path)
        print()
        """

        # Find the bottleneck edge on the path (min capacity)
        bottleneck = RF.getCapacity(path[0], path[1])
        for i in range(1, len(path)-1):
            if RF.getCapacity(path[i], path[i+1]) < bottleneck:
                bottleneck = RF.getCapacity(path[i], path[i+1])

        # Add bottleneck capacity to current max flow
        maxFlow += bottleneck

        # On each edge of the found path, add the bottleneck to the network
        for i in range(len(path)-1):
            prevFlow = FW.getFlow(path[i], path[i+1])
            FW.setFlow(path[i], path[i+1], prevFlow + bottleneck)
        
        # Continue searching for augmented paths on the new residual flow
        RF = residualFlow(FW)
        """
        print("FW")
        FW.printFlows()
        print()
        """
    
    return maxFlow

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

    print(fordFulkerson(F))

        
