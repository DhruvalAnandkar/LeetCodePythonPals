# Problem Type: Hard
# Problem:
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Distribute candies to children based on their ratings.
        This function modifies the candies distribution in-place and returns the minimum number of candies needed.
        """
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize candies array with 1 candy for each child
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Return the total number of candies
        return sum(candies)


# Time Complexity:
# O(n) - We iterate through the ratings array twice, where n is the number of elements.

# Space Complexity:
# O(n) - We use an additional array to keep track of the candies.
