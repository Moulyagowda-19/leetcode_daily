def myAtoi(self, s):
        max = 2**31-1
        min = -2**31
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for i in s:
            if i.isdigit():
                digit = int(i)
                result = result*10 + digit
                if result > max:
                    return max if sign == 1 else min
            else:
                break
        return sign * result
