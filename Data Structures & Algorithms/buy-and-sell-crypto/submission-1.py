class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: initialise two variables, one keeps track of the lowest buying price and one keeps track of the highest selling price 
        # iterate through the array and consider every number as either the buying or selling price. If it's lower than the lowest buying price, set it as the lowest selling price. If it's higher than highest selling price, set it as the highest selling price
        # at the end, return the difference. if the highest selling is lower than the lowest buying, then return 0
        best_margin = 0
        min_value = 101
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                curr_margin = prices[i] - min_value
                if curr_margin > best_margin:
                    best_margin = curr_margin
        return best_margin