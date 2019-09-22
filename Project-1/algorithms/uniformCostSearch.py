class uniformCostSearch:

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
		self.queue = [[{
			"id": start, 
			"cost": 0
		}]]
		self.visited = 0
		self.distance = 0
		
		self.buildGraph()
		self.find(goal)	
		
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
			lowestCost = None		
			lowestIndex = None
			for index, path in enumerate(self.queue):
				if lowestCost is None or path[-1]["cost"] < lowestCost:
					if path[-1]["id"] not in self.explored:
						lowestCost = path[-1]["cost"]
						lowestIndex = index
					
			path = self.queue.pop(lowestIndex)		
			node = path[-1]
			
			if node["id"] not in self.explored:
				for neighbor in self.graph[node["id"]]:
					new_path = list(path)
					new_path.append({
						"id": neighbor["id"],
						"cost": neighbor["distance"] + node["cost"]
					})
					self.queue.append(new_path)
					if neighbor["id"] == goal:
						self.finalPath = new_path
						self.distance = new_path[-1]["cost"]
						return
				self.explored[node["id"]] = None

	def printResult(self):
		print ( \
		"\nUniform Cost Search: \n" \
		"Num nodes visited: " + str(self.visited) + "\n" + \
		"Num nodes on path: " + str(len(self.finalPath)) + "\n" + \
		"Distance (km): " + str(self.distance) + "\n"
		)
		print(self.finalPath)