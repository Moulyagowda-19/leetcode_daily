from collections import Counter
def closeStrings(self, word1, word2):
        # If sets of characters differ → not close
        if set(word1) != set(word2):
            return False

        # Compare sorted frequency values
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        return freq1 == freq2