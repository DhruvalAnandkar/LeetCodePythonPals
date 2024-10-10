# Problem:
# Problem Type: Medium
# You are given an integer array nums. You are initially positioned at the array's first index, and 
# each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: True
# Explanation:
# Jump 1 step from index 0 to index 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: False
# Explanation:
# You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it 
# impossible to reach the last index.
#
# Constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        This function determines if it's possible to reach the last index of the array.
        It takes in an array where each element represents the maximum number of jumps that can be taken from that index.
        """
        # Initialize maxreach to track the farthest index we can reach
        maxreach = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is greater than the maximum reachable index, return False
            if i > maxreach:
                return False
            # Update maxreach with the farthest point we can reach from this index
            maxreach = max(maxreach, i + nums[i])

        # If we can reach or exceed the last index, return True
        return True

# Example usage:
# nums = [2, 3, 1, 1, 4]
# solution = Solution()
# print(solution.canJump(nums))  # Output: True

# Time Complexity:
# O(n) - We iterate through the list once, where n is the number of elements in nums.
#
# Space Complexity:
# O(1) - We are using constant extra space for the maxreach variable.
