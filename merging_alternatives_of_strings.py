def mergeAlternately(self, word1, word2):
        result=[]
        i,j=0,0
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j]) 
            i += 1
            j += 1

        if i < len(word1):
            result.append(word1[i:])   

        if j < len(word2):
            result.append(word2[j:])   

        return "".join(result)
        