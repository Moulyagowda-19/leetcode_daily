from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        r = deque()
        d = deque()
        
        # Fill queues with indices
        for i, ch in enumerate(senate):
            if ch == 'R':
                r.append(i)
            else:
                d.append(i)
        
        # Simulate
        while r and d:
            ri = r.popleft()
            di = d.popleft()
            if ri < di:
                # Radiant acts first and bans this Dire senator.
                # Radiant returns to queue with index + n (next round)
                r.append(ri + n)
            else:
                d.append(di + n)
        
        return "Radiant" if r else "Dire"
