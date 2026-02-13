class Solution:
    def minFlips(self, a, b, c):
        flips = 0
        
        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
            
            if cbit == 0:
                # both a and b must be 0
                flips += abit + bbit
            else:
                # at least one of a or b must be 1
                if abit == 0 and bbit == 0:
                    flips += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips

        
