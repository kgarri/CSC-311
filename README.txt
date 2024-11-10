    
    The overall complexity of  this design isn't overally complex as it uses a graph implementation to repersent the nodes and edges of any network.
By doing so it makes the code more readable and allows for more poweful operations and comparsions to be performed when looping through the nodes on the path.

Djskstra's algorithim complexity 
        Because Djskstra's alogorithim is repersented in a matrix form it only loops for the amount of nodes in the network and not for the edges of the graph.
    By doing so this only leads to a runtime complexity of O(N^2) where N is a node in the graph. The space complexity is O(N) since the matrix only has N items in it.

Distance Vector & Path Vector Algorithim 
        The Distance Vector & Path Vector algorithims are fundementally the same algorthim as they both use edge repersentations of the graph in which to store the data. Now because
    both algorthims only work for a directed graph the space complexity becomes O(E) as it is storing the data in the form of an asjacency list. The runtime is also worse as it becomes
    O(E*N) where E is the edges and N is the nodes in the network, as it is looping through every node in the graph tehn looping through every edge in the graph leading to a double for loop 
    that increases the runtime of this program 
Running the file
    To run the program make sure you have python3 installed on your system and you can run the program by doing python Distance.py <file path> <src node> 
where file path is the system path to a file and src node is an integer, else the program will give errors. 

Participation: 
100% Katherine Garri 
100% Nathan Cobb
100% Duyen Tran 

