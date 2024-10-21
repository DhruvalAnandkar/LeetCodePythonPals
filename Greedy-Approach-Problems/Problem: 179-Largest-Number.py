# Problem Type: Medium
# Problem:
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.
# Example 1:
# Input: nums = [10,2]
# Output: "210"
# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Arrange non-negative integers in nums such that they form the largest number.
        The result is returned as a string.
        """
        # Step 1: Convert numbers to strings
        mapstr = list(map(str, nums))
        
        # Step 2: Sort the numbers based on custom logic
        mapstr.sort(key=lambda x: x * 10, reverse=True)

        # Step 3: Join sorted numbers into a single string
        result = ''.join(mapstr)

        # Step 4: Handle the case of leading zeros
        return result if result[0] != '0' else '0'

# Example usage:
# nums = [3,30,34,5,9]
# output = Solution().largestNumber(nums)
# print(output)  # Output: "9534330"

# Time Complexity:
# O(n log n) - The sorting step takes O(n log n), where n is the number of elements in nums.

# Space Complexity:
# O(n) - We are using additional space for the mapstr list containing string representations of nums.
