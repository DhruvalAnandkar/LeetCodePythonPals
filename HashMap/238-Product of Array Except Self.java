/*
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] prefix = new int[nums.length];
        prefix[0] = nums[0];
        int[] suffix = new int[nums.length];
        suffix[nums.length - 1] = nums[nums.length - 1];
        for (int i = 1; i < nums.length; i++) {
            int j = nums.length - i - 1;
            prefix[i] = prefix[i - 1] * nums[i];
            suffix[j] = suffix[j + 1] * nums[j];
        }

        for (int i = 1; i < nums.length - 1; i++) {
            answer[i] = prefix[i - 1] * suffix[i + 1];
        }
        answer[0] = suffix[1];
        answer[nums.length - 1] = prefix[nums.length - 1 - 1];

        return answer;
    }
}
