def maxProfit(self, prices, fee):
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)   # sell today
            hold = max(hold, cash - price)          # buy today

        return cash
