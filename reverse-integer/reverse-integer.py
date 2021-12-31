class Solution:
    def reverse(self, x: int) -> int:
        if x >=0:
            x_str = str(x)
            x_rev = int(x_str[::-1])
        else:
            x_str = str(x)[1:]
            x_rev = -int(x_str[::-1])
        if x_rev > 2**31-1 or x_rev < -2**31:
            return 0
        return x_rev