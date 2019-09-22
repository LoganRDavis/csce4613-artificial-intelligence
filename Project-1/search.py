from algorithms.breadthFirstSearch import breadthFirstSearch
from algorithms.uniformCostSearch import uniformCostSearch
from algorithms.aStarSearch import aStarSearch

print("\nStarting...")

edgesFilepath = "edges.txt"
heuristicFilepath = "heuristic.txt"

bfs = breadthFirstSearch(edgesFilepath)
bfs.search("105174970", "105012740")
bfs.printResult()

ucs = uniformCostSearch(edgesFilepath)
ucs.search("105174970", "105012740")
ucs.printResult()

ats = aStarSearch(edgesFilepath, heuristicFilepath)
ats.search("105174970", "105012740")
ats.printResult()

print("Done.\n")