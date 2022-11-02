import networkx as nx
import pqueue
import sys

class Dijkstra():
    """Dijkstra's algorithm that works with NetwokX library."""
    def __init__(self, g):
        self.G = g
        self.infinity = sys.maxsize
    
    def path(self, source, target):
        """Main method for finding the shortest path according to Dijkstra's algorithm.
    
        Parameters:
        source (int): source vertex
        target (int): destination vertex
        
        Returns:
        (shortest_path, length, reachable) (tuple):
        shortest_path (list): list of numbers of nodes
        length (int): length of the path
        reachable (boolean): whether or not was the destination vertex reached
        
        """
        nx.set_node_attributes(self.G, self.infinity, 'distance')
        nx.set_node_attributes(self.G, None, 'previous')
        nx.set_node_attributes(self.G, False, 'visited')
        self.G.nodes[source]['distance'] = 0
        shortest_path = []
        pq = pqueue.MinPriorityQueue()
        
        for v in range(self.G.number_of_nodes()):
            pq.insert((self.G.nodes[v]['distance'], v))
        
        while pq.getLength() > 0:
            vert = pq.pop()
            vert_index = vert[1]
            self.G.nodes[vert_index]['visited']=True
            for i in self.G.adj[vert_index]:
                if not self.G.nodes[i]['visited'] and not self.G.edges[vert_index, i]['blocked']:
                    new_dist = self.G.edges[vert_index, i]['lenght'] + self.G.nodes[vert_index]['distance']
                    if new_dist < self.G.nodes[i]['distance']:
                        self.G.nodes[i]['distance'] = new_dist
                        self.G.nodes[i]['previous'] = vert_index
                        pq.update((self.G.nodes[i]['distance'], i))

        path_length = self.G.nodes[target]['distance']
        shortest_path.append(target)
        if self.G.nodes[target]['previous'] == None:
            reachable = False
            path_length = self.infinity
        else:
            reachable = True
            while target != source:
                shortest_path.append(self.G.nodes[target]['previous'])
                target = self.G.nodes[target]['previous']

        shortest_path.reverse()
        return (shortest_path, path_length, reachable)