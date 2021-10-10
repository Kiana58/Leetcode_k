class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # flip
        mat_flip = [row[::-1] for row in image]
        # inverse
        # two for loops in [], add [[  for] for]
        # matrix = [[(1-num) for num in row] for row in mat_flip]
        # or use Bitwise XOR
        matrix = [[(1 ^ num) for num in row] for row in mat_flip]

        return matrix
        
