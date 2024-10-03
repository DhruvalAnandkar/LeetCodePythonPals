# Problem:
# Problem Type: Easy
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should 
# be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k. 
# Change the array nums such that the first k elements of nums contain the unique elements 
# in the order they were present in nums initially. The remaining elements of nums are not 
# important as well as the size of nums.
# 
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 
# 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 
# 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
# - 1 <= nums.length <= 3 * 10^4
# - -100 <= nums[i] <= 100
# - nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from the sorted array nums in-place.
        The function modifies nums and returns the number of unique elements in nums.
        """
        # Explanation:
        # We will use a pointer k to track the index of the next unique element.
        # Iterate through the array, and whenever we find an element that is not equal to 
        # the previous one, we place it at index k and increment k.

        if not nums:  
            return 0  # If the array is empty, return 0

        k = 1  # Start from the second element, as the first element is always unique
        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[i - 1]:  # Check if the current element is different from the previous one
                nums[k] = nums[i]  # Assign the current element to the position k
                k += 1  # Move the pointer for the next unique position
        
        return k  # Return the count of unique elements

# Example usage:
# nums = [0,0,1,1,1,2,2,3,3,4]
# k = Solution().removeDuplicates(nums)
# print(k)  # Output: 5
# print(nums)  # Output: [0,1,2,3,4,_,_,_,_,_] (the actual values may differ in the remaining spaces)

# Time Complexity:
# O(n) - We iterate through the array once, where n is the number of elements in nums.

# Space Complexity:
# O(1) - We are modifying the array in-place without using additional space.
