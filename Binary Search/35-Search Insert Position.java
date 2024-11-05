/*
https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104


*/

class Solution {
    public int searchInsert(int[] nums, int target) {
        int offset = 0;
        if (target < nums[0]) return 0;
        if (target > nums[nums.length - 1]) return nums.length;
        while (true) {
            int i = Math.max(0, (nums.length / 2) - 1);
            if (nums[i] == target)
                return i;
            else if (nums.length == 1) {
                return (target > nums[i]) ? (i + 1 + offset) : (i - 1 + offset);
            } else if (target > nums[i]) {
                offset += i + 1;
                nums = Arrays.copyOfRange(nums, i + 1, nums.length);
            } else {
                nums = Arrays.copyOfRange(nums, 0, i);
            }
        }
    }
}
