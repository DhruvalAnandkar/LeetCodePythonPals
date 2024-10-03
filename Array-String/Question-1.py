# Problem:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The result should be stored in-place in nums1, which has enough space to hold the combined elements.
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Constraints:
# - nums1.length == m + n
# - nums2.length == n
# - 0 <= m, n <= 200
# - -10^9 <= nums1[i], nums2[j] <= 10^9


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums1 and nums2 into nums1 in-place.
        The first m elements in nums1 and all elements of nums2 are sorted,
        and nums1 has enough space to hold both nums1 and nums2 (with n extra 0s at the end).
        """
        # Explanation:
        # Append elements of nums2 into nums1 starting at index m, 
        # then sort the entire nums1 array to make it non-decreasing.
        
        i = 0
        j = m
        for i in range(n):
            nums1[j] = nums2[i]
            j += 1
        nums1.sort()  # Sort the merged array

# Example usage:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Solution().merge(nums1, m, nums2, n)
# print(nums1)  # Output: [1,2,2,3,5,6]

# Time Complexity:
# O((m + n) log(m + n)) - The merging itself is O(n), but sorting the array takes O((m + n) log(m + n)).

# Space Complexity:
# O(1) - We are modifying the array in-place without any additional space.
