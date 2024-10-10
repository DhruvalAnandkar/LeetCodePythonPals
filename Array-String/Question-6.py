# Problem:
# Problem Type: Medium
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 step to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 step to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
# Follow up: 
# Could you solve the problem in O(1) extra space?

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        This function rotates the array `nums` to the right by `k` steps.
        The rotation is done in-place with O(1) extra space.
        """
        # Get the length of the array
        n = len(nums)

        # If k is greater than the array length, we use k % n (as rotating by n steps brings us back to the same array)
        k = k % n

        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])

# Example usage:
# nums = [1,2,3,4,5,6,7]
# k = 3
# solution = Solution()
# solution.rotate(nums, k)
# print(nums)  # Output: [5,6,7,1,2,3,4]

# Time Complexity:
# O(n) - Each reverse operation takes O(n), and we perform three reverse operations, so it's linear overall.
#
# Space Complexity:
# O(1) - The rotation is done in-place without using any additional space, apart from a few temporary variables.
