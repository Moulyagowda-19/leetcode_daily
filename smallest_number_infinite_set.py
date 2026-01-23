import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.in_heap = set()

    def popSmallest(self):
        if self.heap:
            val = heapq.heappop(self.heap)
            self.in_heap.remove(val)
            return val
        
        val = self.curr
        self.curr += 1
        return val

    def addBack(self, num):
        if num < self.curr and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)
