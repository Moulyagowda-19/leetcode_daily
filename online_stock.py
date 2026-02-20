class StockSpanner:

    def __init__(self):
        # stack will store (price, span)
        self.stack = []

    def next(self, price):
        span = 1

        # merge previous smaller prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span
