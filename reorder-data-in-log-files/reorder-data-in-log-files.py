class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # inplace ordering
#         # step 1: order letter and digit, put digit after letter, keep same order for digit, count # of letter
#         n, idx = len(logs), 0
        
#         while idx < n:
#             if logs[idx][0] == 'l':
#                 idx += 1
#             else:
#                 while logs[idx][0] == 'd':
#                     logs[idx], logs[idx+1] = logs[idx+1], logs[idx]
                    
                    
#         # step 2: order letter part

        minHeap = []
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                heapq.heappush(minHeap, (log.split()[1:], log.split()[0]))
                
        while minHeap:
            list_, header  = heapq.heappop(minHeap)
            letter_logs.append(header + ' ' + ' '.join(list_))
            
        
        return letter_logs + digit_logs
                    
        