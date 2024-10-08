# Problem:
# Problem Type: Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If no profit is possible, return 0.
#
# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation:
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation:
# In this case, no transactions are done and the max profit = 0.
#
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This function calculates the maximum profit from buying and selling a stock once.
        It takes in an array of stock prices where prices[i] represents the price of the stock on the ith day.
        """
        # Initialize two variables: left for the buying day, max_profit for tracking the maximum profit
        left = 0  # Buy day index
        max_profit = 0  # Maximum profit initialized to 0

        # Loop through the prices starting from the second day
        for right in range(1, len(prices)):
            # If current selling day (right) price is greater than buying day (left) price
            if prices[right] > prices[left]:
                # Calculate the current profit and update max_profit if it's larger
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # If current price is less than or equal to buying day price, update the buying day (left)
                left = right

        return max_profit

# Example usage:
# prices = [7, 1, 5, 3, 6, 4]
# solution = Solution()
# print(solution.maxProfit(prices))  # Output: 5

# Time Complexity:
# O(n) - We iterate through the list once, where n is the number of elements in prices.

# Space Complexity:
# O(1) - We are only using a few extra variables (left, max_profit) and modifying the list in place, so the space usage is constant.
