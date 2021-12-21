class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # method: topolotical sort
        
        
        # step 1: build the graph with hashmap, key: course; values: list of prerequistes
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        for prereq in prerequisites:
            curr, pre = prereq[0], prereq[1]
            graph[pre].append(curr)
            indegree[curr] += 1
            
        # step 2: find root of graph with indegree == 0, inilitize the source
        source = deque()
        
        for key in indegree:
            if indegree[key] == 0:
                source.append(key)
                
        # step 3: topological sorting
        sortedCourses = []
        while source:
            pre = source.popleft()
            sortedCourses.append(pre)
            for curr in graph[pre]:
                indegree[curr] -= 1
                if indegree[curr] == 0:
                    source.append(curr)
                    
        return len(sortedCourses) == numCourses
                
        
        