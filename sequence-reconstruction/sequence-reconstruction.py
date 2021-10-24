class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # org is topo sort of seqs
        # build graph
        graph = self.build_graph(seqs)
        topo_order = self.topo_sort(graph)
        return topo_order == org
    
    def build_graph(self, seqs):
        # in graph dict, each node as key, and a set with all node after that node
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i-1]].add(seq[i])
                
        return graph
    
    def get_indegrees(self, graph):
        
        # intialize indegrees dict, every node, has a value of indegree
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
    
    def topo_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        # initiaze the queue
        queue = collections.deque()
        
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
                
        topo_order = []
        
        while queue:
            # very important!!!!
            if len(queue) > 1:
                # then there is more than one topo orders
                return None
            node = queue.popleft() # always one node, could use list instead of deque
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
        
        return None