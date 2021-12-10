class Solution:
    def numberToWords(self, num: int) -> str:
        # method: split into 000; group together
        
        # edge case
        if num == 0: 
            return 'Zero'
        
        # split list for num
        list_split = []
        
        while num > 0:
            num_split, num = num % 1000, num // 1000
            list_split.append(str(num_split))
            
        list_split.reverse()
        
        # step 1: help fun to read num < 1000
        
        identifiers = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred'
        }
        
        def helper(num_split):
            res = ''
            _n = len(num_split)
            if _n == 3:
                if int(num_split[0]) != 0:
                    res += identifiers[int(num_split[0])] + ' Hundred '
                    
                num_split = num_split[1:]
                _n = len(num_split)
                
            def helper_2digits(num_split):
                if _n == 1:
                    return identifiers[int(num_split)]
                elif _n == 2:
                    if int(num_split) in identifiers:
                        return identifiers[int(num_split)]
                    else:
                        return identifiers[int(num_split[0]+'0')] + ' ' +  identifiers[int(num_split[1])]
                else:
                    return ''
            return res + helper_2digits(num_split)
        
        # step 2: billion, million...        
        result = ''
        
        # billions  = len(list_split) == 4
        # millions  = len(list_split) == 3
        # thousands = len(list_split) == 2
        
        digits = list_split[0]
        if int(digits) > 0 and len(list_split) == 4:
            result += helper(digits) + ' Billion '
            list_split.pop(0)
            digits = list_split[0]
        if len(list_split) == 3:
            if int(digits) > 0:
                result += helper(digits) + ' Million '
            list_split.pop(0)
            digits = list_split[0]
        if len(list_split) == 2:
            if int(digits) > 0:
                result += helper(digits) + ' Thousand '
            list_split.pop(0)
            digits = list_split[0]
        if int(digits) > 0:
            result += helper(digits)
        
            
        return result.replace('  ', ' ').strip()
                
            