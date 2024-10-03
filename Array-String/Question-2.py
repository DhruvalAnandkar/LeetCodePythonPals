# Problem: 
#Problem Type: Easy
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k. 
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# 
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#
# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 1, 3, and 4.
#
# Constraints:
# - 0 <= nums.length <= 100
# - 0 <= nums[i] <= 50
# - 0 <= val <= 100

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in nums in-place.
        The function modifies nums and returns the number of elements remaining that are not equal to val.
        """
        # Explanation:
        # We will use a pointer k to track the index of the elements that are not equal to val.
        # Iterate through the array, and whenever we find an element not equal to val,
        # we place it at index k and increment k.

        k = 0  # Pointer for the position of the next non-val element
        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k += 1  # Move the pointer for the next valid position
        return k  # Return the count of elements not equal to val

# Example usage:
# nums = [3,2,2,3], val = 3
# k = Solution().removeElement(nums, val)
# print(k)  # Output: 2
# print(nums)  # Output: [2,2,_,_] (the actual values may differ in the remaining spaces)

# Time Complexity:
# O(n) - We iterate through the array once, where n is the number of elements in nums.

# Space Complexity:
# O(1) - We are modifying the array in-place without using additional space.
