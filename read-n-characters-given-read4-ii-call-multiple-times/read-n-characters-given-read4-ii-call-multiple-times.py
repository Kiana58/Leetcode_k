# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = []
        
    def read(self, buf: List[str], n: int) -> int:
        tot_char_read = 0
        nb_char_read = 4
        buf4 = [""]*4
        while tot_char_read < n and nb_char_read > 0:
            # we write from queue to buff until we have read the required amount of chars
            if len(self.q) > 0:
                buf[tot_char_read] = self.q.pop(0)
                tot_char_read += 1
            # If queue is empty, we refill it by calling read4
            else:
                nb_char_read = read4(buf4)
                self.q += buf4[:nb_char_read]
        return tot_char_read
