"""
Implementation of Ford-Fulkerson algorithm for finding max flow
"""
import sys
sys.path.append('.')

from graphs.graphtraversals import dfs
from flownetwork import FlowNetwork, residualFlow, importFNFromFile

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
    
    return maxFlow

if __name__ == "__main__":
    F = importFNFromFile("max_flow/examples/1.txt")
    print(fordFulkerson(F))

    F = importFNFromFile("max_flow/examples/2.txt")
    print(fordFulkerson(F))

        
