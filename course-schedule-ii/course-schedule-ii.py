from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # graph, list of list, every list for every node/class, append courses after taking that class
        graph = [[] for _ in range(numCourses)]
        
        # every node: indegree
        in_degree = [0] * numCourses
        
        # build graph and in_degree
        for post, pre in prerequisites:
            graph[pre].append(post)
            in_degree[post] += 1
            
        # Initizlize queue, put node when indegree is 0
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # num of courses taken
        num_taken = 0
        # result with courses ordered
        topo_order = []
        
        # pop course from queue, delete the indegree from the course, find other courses if indegree is 0
        while queue:
            now_pos = queue.popleft()
            topo_order.append(now_pos)
            num_taken += 1
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
                    
        return topo_order if num_taken == numCourses else []
            
            
            