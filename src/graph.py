import networkx as nx
import matplotlib.pyplot as plt
import random
import dijkstra

class Greedy():
    """Greedy strategy that solves the Canadian traveller problem.

    When there is a blockage on the shortest path resolved by Dijktra's algorighm,
    the traveller goes by the newly resolved shortest path in which the edge with 
    the blockage was not considered.
    
    """
    def __init__(self, graph):
        self.G = graph.copy()
        self.f = plt.figure(figsize=(4,4), dpi=100)

    def greedy(self, source, destination):
        """Main method for greedy strategy.

        Parameters:
        source (int): number of source vertex
        destination (int): number of destination vertex

        Returns:
        greedyPath (tuple):
            open_path (list): list of numbers of vertices from the source to the destination
            distance (int): lenght of the path
            self.G (NetwokX graph): graph with the shown path
            f (matplotlib figure): figure with the graph
        
        """
        d = dijkstra.Dijkstra(self.G)
        open_path = []
        distance = 0
        short_path = d.path(source, destination)
        if short_path[2]:
            #open_path.append(short_path[0][0])
            open_path.append(short_path[0][0])
            j = 0

            while open_path[-1] != destination:
                if self.G.edges[short_path[0][j], short_path[0][j+1]]['color']=="red":
                    self.G.edges[short_path[0][j], short_path[0][j+1]]['blocked']=True
                    #self.G.remove_edge(short_path[0][j], short_path[0][j+1])
                    source = short_path[0][j]
                    short_path = d.path(source, destination)
                    if short_path[2] == False:
                        break
                    j = 0
                else:
                    distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                    j += 1
                    open_path.append(short_path[0][j])   
                    self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="green"
            for i in range(len(open_path)-2):   
                self.G.edges[open_path[i], open_path[i+1]]['color']="green"

        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
            
        # colors = nx.get_edge_attributes(self.G,'color').values()
        # pos = nx.circular_layout(self.G)
        # nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        # plt.show()
            
        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        #f = plt.Figure()
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        #plt.show()

        greedyPath = (open_path, distance, self.G, self.f)
        return greedyPath

class Reposition():
    """Reposition strategy that solves the Canadian traveller problem.

    When there is a blockage on the shortest path resolved by Dijktra's algorighm,
    the traveller goes back to the source vertex and goes by the newly resolved
    shortest path in which the edge with the blockage was not considered.

    """
    def __init__(self, graph):
        self.G = graph.copy()
        self.f = plt.figure(figsize=(4,4), dpi=100)

    def reposition(self, source, destination):
        """Main method for the reposition strategy.

        Parameters:
        source (int): number of source vertex
        destination (int): number of destination vertex

        Returns:
        greedyPath (tuple):
            open_path (list): list of numbers of vertices from the source to the destination
            distance (int): lenght of the path
            self.G (NetwokX graph): graph with the shown path
            f (matplotlib figure): figure with the graph
        
        """
        d = dijkstra.Dijkstra(self.G)
        open_path = []
        distance = 0
        non_blocked_dist = 0
        short_path = d.path(source, destination)
        if short_path[2]:
            #open_path.append(short_path[0][0])
            open_path.append(short_path[0][0])
            j = 0
            while open_path[-1] != destination:
                if self.G.edges[short_path[0][j], short_path[0][j+1]]['color']=="red":
                    self.G.edges[short_path[0][j], short_path[0][j+1]]['blocked']=True
                    distance += non_blocked_dist
                    non_blocked_dist = 0
                    #self.G.remove_edge(short_path[0][j], short_path[0][j+1])
                    source = short_path[0][0]
                    if open_path[-1] != source:
                        open_path.append(source)
                    short_path = d.path(source, destination)
                    if short_path[2] == False:
                        break
                    j = 0
                else:
                    distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                    non_blocked_dist += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                    j += 1
                    open_path.append(short_path[0][j])   
                    self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="green"
        
        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        # plt.show()
        
        repositionPath = (open_path, distance, self.G, self.f)
        return repositionPath

class Comparison():
    """Comparison strategy that solves the Canadian traveller problem.

    When there is a blockage on the shortest path resolved by Dijktra's algorighm,
    the traveller decides whether to use greedy or reposition strategygoes according
    to which strategy gives the better result.

    """
    def __init__(self, graph):
        self.G = graph.copy()
        self.f = plt.figure(figsize=(4,4), dpi=100)

    def comparison(self, source, destination):
        """Main method for comparison strategy.

        Parameters:
        source (int): number of source vertex
        destination (int): number of destination vertex

        Returns:
        greedyPath (tuple):
            open_path (list): list of numbers of vertices from the source to the destination
            distance (int): lenght of the path
            self.G (NetwokX graph): graph with the shown path
            f (matplotlib figure): figure with the graph
        
        """
        d = dijkstra.Dijkstra(self.G)
        open_path = []
        distance = 0
        non_blocked_dist = 0
        short_path = d.path(source, destination)
        if short_path[2]:
            #open_path.append(short_path[0][0])
            open_path.append(short_path[0][0])
            j = 0

            while open_path[-1] != destination:
                if self.G.edges[short_path[0][j], short_path[0][j+1]]['color']=="red":
                    self.G.edges[short_path[0][j], short_path[0][j+1]]['blocked']=True
                    #self.G.remove_edge(short_path[0][j], short_path[0][j+1])
                    sourceGreedy = short_path[0][j]
                    sourceReposition = 0
                    short_pathGreedy = d.path(sourceGreedy, destination)
                    short_pathReposition = d.path(sourceReposition, destination)
                    if short_pathGreedy[1] <= short_pathReposition[1]:
                        short_path = short_pathGreedy
                        if short_path[2] == False:
                            break
                    else:
                        distance += non_blocked_dist
                        non_blocked_dist = 0
                        short_path = short_pathReposition
                        if short_path[2] == False:
                            break
                        distance += non_blocked_dist
                        non_blocked_dist = 0
                        open_path.append(sourceReposition)
                    j = 0
                else:
                    distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                    non_blocked_dist += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                    j += 1
                    open_path.append(short_path[0][j])                
                    self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="green"
        
        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        # plt.show()

        return (open_path, distance, self.G, self.f)

class Waiting():
    """Waiting strategy that solves the Recoverable Canadian traveller problem.

    When there is a blockage on the shortest path resolved by Dijktra's algorighm,
    the traveller pays the penalty (waits for the road to be opened again) and then
    continues.

    """
    def __init__(self, graph):
        self.G = graph.copy()
        self.f = plt.figure(figsize=(4,4), dpi=100)
    
    def waiting(self, source, destination):
        """Main method for reposition algorighm.

        Parameters:
        source (int): number of source vertex
        destination (int): number of destination vertex

        Returns:
        greedyPath (tuple):
            open_path (list): list of numbers of vertices from the source to the destination
            distance (int): lenght of the path
            penalty (int): value of the total penalty paid by the traveller
            self.G (NetwokX graph): graph with the shown path
            f (matplotlib figure): figure with the graph
        
        """
        d = dijkstra.Dijkstra(self.G)
        #distance = 0
        penalty = 0
        short_path = d.path(source, destination)

        for j in range(len(short_path[0])-1):
            if self.G.edges[short_path[0][j], short_path[0][j+1]]['color']=="red":
                self.G.edges[short_path[0][j], short_path[0][j+1]]['blocked']=True
                penalty = penalty + self.G.edges[short_path[0][j], short_path[0][j+1]]['penalty']
                #distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                self.G.edges[short_path[0][j], short_path[0][j+1]]['color']="blue"
            else:
                #distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                self.G.edges[short_path[0][j], short_path[0][j+1]]['color']="green"
        
        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        # plt.show()

        return (short_path[0], short_path[1], penalty, self.G, self.f)

class RecoveryGreedy():
    """Recovery greedy strategy that solves the Recoverable Canadian traveller problem.

    When there is a blockage on the shortest path resolved by Dijktra's algorighm,
    the traveller decides whtether to pay the penalty (wait for the road to be opened 
    again) or go by the new shortest path and bypass the blocked road.
    
    """
    def __init__(self, graph):
        self.G = graph.copy()
        self.f = plt.figure(figsize=(4,4), dpi=100)

    def recoveryGreedy(self, source, destination):
        """Main method for reposition algorighm.

        Parameters:
        source (int): number of source vertex
        destination (int): number of destination vertex

        Returns:
        greedyPath (tuple):
            open_path (list): list of numbers of vertices from the source to the destination
            distance (int): lenght of the path
            penalty (int): value of the total penalty paid by the traveller
            self.G (NetwokX graph): graph with the shown path
            f (matplotlib figure): figure with the graph

        """
        d = dijkstra.Dijkstra(self.G)
        open_path = []
        distance = 0
        penalty = 0
        short_path = d.path(source, destination)
        open_path.append(short_path[0][0])
        j = 0
        reachable = short_path[2]

        while open_path[-1] != destination and reachable:
            if self.G.edges[short_path[0][j], short_path[0][j+1]]['color']=="red":
                self.G.edges[short_path[0][j], short_path[0][j+1]]['blocked']=True
                #self.G.remove_edge(short_path[0][j], short_path[0][j+1])
                path_greedy = d.path(short_path[0][j], destination)
                if short_path[0][j+1] != destination:
                    path_wait = d.path(short_path[0][j+1], destination)
                    if path_greedy[1] <= path_wait[1] + self.G.edges[short_path[0][j], short_path[0][j+1]]['penalty'] + self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']:
                        short_path = path_greedy
                        reachable = short_path[2]
                        j = 0
                    else:
                        penalty += self.G.edges[short_path[0][j], short_path[0][j+1]]['penalty']
                        distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                        j += 1
                        open_path.append(short_path[0][j])   
                        self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="blue"
                else:
                    if path_greedy[1] <= self.G.edges[short_path[0][j], short_path[0][j+1]]['penalty'] + self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']:
                        short_path = path_greedy
                        reachable = short_path[2]
                        j = 0
                    else:
                        penalty += self.G.edges[short_path[0][j], short_path[0][j+1]]['penalty']
                        distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                        j += 1
                        open_path.append(short_path[0][j])   
                        self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="blue"
            else:
                distance += self.G.edges[short_path[0][j], short_path[0][j+1]]['lenght']
                j += 1
                open_path.append(short_path[0][j])   
                self.G.edges[short_path[0][j-1], short_path[0][j]]['color']="green"
        # for i in range(len(open_path)-2):   
        #     self.G.edges[open_path[i], open_path[i+1]]['color']="green"
        
        # colors = nx.get_edge_attributes(self.G,'color').values()
        # #pos = nx.circular_layout(self.G)
        # labels = {e: self.G.get_edge_data(e[0], e[1])["lenght"] for e in self.G.edges()}
        # nx.draw(self.G, pos=nx.spring_layout(self.G), edge_color=colors, with_labels=True, node_color='lightgreen')
        # nx.draw_networkx_edge_labels(self.G, pos=nx.circular_layout(self.G), edge_labels=labels)
        # plt.show()

        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')

        return (open_path, distance, penalty, self.G, self.f)

class Graph():
    """The initial unresolved graph.
    
    """
    def __init__(self):
        self.G = nx.Graph()
        self.f = plt.figure(figsize=(4,4), dpi=100)
    
    def removeEdge(self, source, dest):
        try:
            self.G.remove_edge(source, dest)
        except:
            print("bad parameters")


    def addEdge(self, source, dest, l, p):
        """Method for adding the edge.

        Parameters:
        source (int): number of the source vertex of the edge
        dest (int): number of the destination vertex of the edge
        l (int): lenght of the edge
        p (int): penalty that must be paid to use blocked edge
        
        """
        try:
            if p != 0:
                clr = "red"
            else:
                clr = "black"
            self.G.add_edge(source, dest, lenght=l, penalty=p, color=clr, blocked=False)
        except:
            print("bad parameters")
    
    def changeEdge(self, source, dest, l, p):
        """Method for changing the values of the edge.

        Parameters:
        source (int): number of the source vertex of the edge
        dest (int): number of the destination vertex of the edge
        l (int): changed lenght of the edge
        p (int): changed penalty that must be paid to use blocked edge
        
        """        
        try:
            self.G.remove_edge(source, dest)
            self.addEdge(source, dest, l, p)
        except:
            print("bad parameters")
    
    def addBlockage(self, source, dest, p):
        """Method for adding blockages to the graph.

        Parameters:
        source (int): number of the source vertex of the blocked edge
        dest (int): number of the destination vertex of the blocked edge
        p (int): changed penalty that must be paid to use blocked edge
        
        """       
        try:
            self.G.edges[source, dest]['color']="red"
            self.G.edges[source, dest]['penalty']=p
        except:
            print("bad parameters")
    
    def generateRandom(self, vert, dir, p):
        """Method which uses NetworkX function for generating random graph.

        Parameters:
        vert (int): number of the source vertex of the edge
        dir (bool): set True for directed graph and False for undirected
        p (float): probability of blocked edges <0;1>
        
        """       
        self.G = nx.erdos_renyi_graph(vert, 0.4, seed=None, directed=dir)
        nx.set_edge_attributes(self.G, False, 'blocked')
        nx.set_edge_attributes(self.G, 0, 'penalty')
        nx.set_edge_attributes(self.G, "black", 'color')

        list_edges = list(self.G.edges)
        for e in list_edges:
            l = random.randint(1, 50)
            self.G.edges[e[0], e[1]]['lenght']=l
            #print(ba.edges[e[0], e[1]]['length'])

        num_blocked_edges = int(len(list_edges)*p)
        blocked_edges = []
        for i in range(num_blocked_edges):
            rand_edge = random.randint(0, len(list_edges)-1)
            while rand_edge in blocked_edges:
                rand_edge = random.randint(0, len(list_edges)-1)
            blocked_edges.append(rand_edge)
            self.G.edges[list_edges[rand_edge][0], list_edges[rand_edge][1]]['color']="red"
            self.G.edges[list_edges[rand_edge][0], list_edges[rand_edge][1]]['penalty']=random.randint(1,10)
        self.drawGraph()

    def drawGraph(self):
        """Draws graph to the Matlotlib's figure
        
        """
        plt.close('all')
        self.f = plt.figure(figsize=(4,4), dpi=100)
        colors = nx.get_edge_attributes(self.G,'color').values()
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos, edge_color=colors, with_labels=True, node_color='lightgreen')
        # plt.show()