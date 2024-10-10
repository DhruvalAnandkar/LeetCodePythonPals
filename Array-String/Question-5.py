# Problem:
# Problem Type: Easy
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        This function returns the majority element in the list, which is defined as the element
        that appears more than n // 2 times in the list.
        It uses the Boyer-Moore Voting Algorithm to solve the problem in linear time and O(1) space.
        """
        # Initialize two variables: count for tracking the number of occurrences,
        # and el for the current candidate element.
        count = 0
        el = 0

        # Phase 1: Finding a candidate for the majority element.
        for i in range(len(nums)):
            if count == 0:
                # If count drops to 0, pick the current element as the candidate.
                el = nums[i]
                count = 1
            elif nums[i] == el:
                # If the current element is the same as the candidate, increase the count.
                count += 1
            else:
                # If it's a different element, decrease the count.
                count -= 1

        # Phase 2: Verifying that the candidate is the majority element.
        nbycheck = 0
        for i in range(len(nums)):
            if nums[i] == el:
                nbycheck += 1

        # Check if the candidate appears more than n // 2 times.
        if nbycheck > len(nums) // 2:
            return el
        else:
            return -1

# Example usage:
# nums = [2,2,1,1,1,2,2]
# solution = Solution()
# print(solution.majorityElement(nums))  # Output: 2

# Time Complexity:
# O(n) - We traverse the array twice (once to find the candidate and once to verify it), where n is the number of elements.
#
# Space Complexity:
# O(1) - We are only using constant extra space for variables (count, el).
