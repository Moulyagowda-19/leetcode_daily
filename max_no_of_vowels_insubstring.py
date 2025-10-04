def maxVowels(self, s, k):
        vowels = set("aeiou")
        count = 0
        max_vowels = 0

        # first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_vowels = count

        # sliding window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_vowels = max(max_vowels, count)

        return max_vowels
