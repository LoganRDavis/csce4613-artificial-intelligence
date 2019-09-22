class breadthFirstSearch:

	def __init__(self, edgesFilepath):
		self.edgesFilepath = edgesFilepath
		self.graph = {}
		self.explored = {}
		self.queue = []
		self.visited = 0
		self.distance = 0
		self.finalPath = []
		
	def search(self, start, goal):
		self.graph = {}
		self.explored = {}
		self.queue = [[start]]
		self.visited = 0
		self.distance = 0
		
		self.buildGraph()
		self.find(goal)	
		self.calculateDistance(goal)
		
	def buildGraph(self):
		with open(self.edgesFilepath) as infile:
			for cnt, line in enumerate(infile):
				edge = line.rstrip().split(" ")
				if edge[0] not in self.graph:
					self.graph[edge[0]] = []
				if edge[1] not in self.graph:
					self.graph[edge[1]] = []
				self.graph[edge[0]].append({
					"id": edge[1],
					"distance": float(edge[2])
				})
				self.graph[edge[1]].append({
					"id": edge[0],
					"distance": float(edge[2])
				})
				
	def find(self, goal):
		while self.queue:
			self.visited += 1
			path = self.queue.pop(0)
			node = path[-1]
			if node not in self.explored:
				for neighbor in self.graph[node]:
					new_path = list(path)
					new_path.append(neighbor["id"])
					self.queue.append(new_path)
					if neighbor["id"] == goal:
						self.finalPath = new_path
						return
				self.explored[node] = None
		
	def calculateDistance(self, goal):
		for index, nodeId in enumerate(self.finalPath):
			if nodeId != goal:
				for graphNeighbor in self.graph[nodeId]:
					if graphNeighbor["id"] == self.finalPath[index + 1]:
						self.distance += graphNeighbor["distance"]
						break
		
	def printResult(self):
		print ( \
		"\nBreadth First Search: \n" \
		"Num nodes visited: " + str(self.visited) + "\n" + \
		"Num nodes on path: " + str(len(self.finalPath)) + "\n" + \
		"Distance (km): " + str(self.distance) + "\n"
		)
		print(self.finalPath)