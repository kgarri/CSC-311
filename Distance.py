import sys 
class Graph():
    def __init__(self, vertices,edges):
        self.V = vertices 
        self.matrix_graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.parents = [-1] * vertices
        self.edges_graph = edges
    

    def printSolution(self, dist, alg, src): # function for printing the solution
        print(alg)
        for node in range(self.V):
            self.arr =[]
            if node != src: 
                print(f"Shortest path to node {node} is {src}->", end="")
                self.print_path(node) 
                print(f"{"->".join([str(i) for i in  self.arr])}",end="")
                print(f" with cost {dist[node]}")

    def distanceVector(self,src): #distance vector algorithim, that also stores the path information
        dist = [sys.maxsize]*self.V
        dist[src] = 0
        self.parents = [-1] * self.V
        for i in range(self.V -1):
            for u,v,w in self.edges_graph:
                tmp = dist.copy()[v]
                dist[v] = min(dist[v], dist[u] + w)
                if tmp > dist[u]+w:
                    self.parents[v] = u 
                    
                
        self.printSolution(dist, "Distance Vector Routing",src)

            
    def print_path(self,node): #function to print the path, essentially tree transversal to return an arr that can be sused to show the path
        if self.parents[node] == -1:
            return 
        self.print_path(self.parents[node])
        self.arr.append(node)

    def minDistanceDjkstra(self, dist, sptSet): #the minnum distance  of Dijkstra used to find the next min index 
        min = sys.maxsize 
        min_index = -1 
        for u in range(self.V):
            if dist[u]< min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src): #dijkstra's algorithim itself  also stores the path information 
        dist = [sys.maxsize] * self.V
        dist[src] = 0 
        self.parents[src] = -1
        sptSet = [False]* self.V 
        

        for cout in range(self.V): 
            x = self.minDistanceDjkstra(dist, sptSet)

            sptSet[x] = True

            for y in range(self.V): 
                if self.matrix_graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.matrix_graph[x][y]: 
                        self.parents[y] = x
                        dist[y] = dist[x] + self.matrix_graph[x][y]

    
        self.printSolution(dist, "Dijkstra's Algorithim",src)
    def pathVector(self,src): # path vector algorithim is used to show the best path the network could possiblly take
        path = [sys.maxsize]*self.V
        self.parents = [-1] * self.V
        path[src] = 0
        for i in range(self.V -1):
            for u,v,w in self.edges_graph:
                tmp = path.copy()[v]
                path[v] = min(path[v], path[u] + w)
                if tmp > path[u]+w:
                    self.parents[v] = u 
                    
                
        self.printSolution(path, "Path Vector Routing", src)

def parse_init(filename):#this is or intiliazing matrix, it returns the node/vertices number a matrix graph repersenation and an edge graph repersentation  
    with open(filename, 'r') as file:
        arrLen = int(file.readline().strip())
        cols = []
        edges = []
        for j in range(arrLen):
            row = []
            for i in range(arrLen):
                row.append(0)
            cols.append(row)
        for line in file.readlines()[0:]:
            line.strip()
            args = line.split(' ')
            node1 = int(args[0])
            node2 = int(args[1])
            dist = int(float(args[2]))
            cols[node1].pop(node2)
            cols[node1].insert(node2, dist)
            cols[node2].pop(node1)
            cols[node2].insert(node1, dist)
            cols[node1].pop(node1)
            cols[node1].insert(node1, 0)
            cols[node2].pop(node2)
            cols[node2].insert(node2, 0)
            edges.append((node1,node2,dist))
            edges.append((node2, node1, dist))
    return(arrLen , cols, edges)


if __name__ == "__main__":
    filename = sys.argv[1]
    src = int(sys.argv[2])
    node_num, matrix, edges = parse_init(filename)
    graph = Graph(node_num,edges)
    graph.matrix_graph = matrix
    graph.dijkstra(src)
    graph.distanceVector(src)
    graph.pathVector(src)
    
    







