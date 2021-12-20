class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def helper_2digit(num, idx):
            return ord(num[idx]) - ord('0') if idx >=0 else 0
        idx_n, idx_m, idx = len(num1)-1, len(num2)-1, 0
        res = 0
        while idx_n >= 0 or idx_m >=0:
            num1_idx = helper_2digit(num1, idx_n)
            num2_idx = helper_2digit(num2, idx_m)
            # print("num1_idx, num2_idx: ", num1_idx, num1_idx)
            # print("idx_n, idx_m: ", idx_n, idx_m)
            # if idx_n < 0:
            #     num1_idx = 0
            # if idx_m < 0:
            #     num2_idx = 0
            res += 10 ** idx * (num1_idx + num2_idx)
            idx_n -= 1
            idx_m -= 1
            idx += 1

        return str(res)