# Problem:
# Problem Type: Medium
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
# such that each unique element appears at most twice. The relative order of the elements should 
# be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead 
# have the result be placed in the first part of the array nums. More formally, if there are k 
# elements after removing the duplicates, then the first k elements of nums should hold the 
# final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array 
# in-place with O(1) extra memory.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 
# 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 
# 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
# - 1 <= nums.length <= 3 * 10^4
# - -10^4 <= nums[i] <= 10^4
# - nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from the sorted array nums such that each unique element appears at most twice.
        The function modifies nums and returns the number of elements remaining that meet the criteria.
        """
        # Explanation:
        # We will use a pointer k to track the index of the next valid position 
        # for the unique elements and a count variable to track occurrences of each element.
        
        if len(nums) == 0:
            return 0  # If the array is empty, return 0
        
        k = 1  # Start from the second element, since the first element is always unique
        count = 1  # Initialize the count of the current element occurrences

        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] == nums[i - 1]:
                count += 1  # Increment the count for the current element
            else:
                count = 1  # Reset the count for a new element
            
            if count <= 2:  # If the count is less than or equal to 2, we keep the element
                nums[k] = nums[i]
                k += 1  # Move the pointer for the next valid position
        
        return k  # Return the count of elements that meet the criteria

# Example usage:
# nums = [1,1,1,2,2,3]
# k = Solution().removeDuplicates(nums)
# print(k)  # Output: 5
# print(nums)  # Output: [1,1,2,2,3,_] (the actual values may differ in the remaining spaces)

# Time Complexity:
# O(n) - We iterate through the array once, where n is the number of elements in nums.

# Space Complexity:
# O(1) - We are modifying the array in-place without using additional space.
