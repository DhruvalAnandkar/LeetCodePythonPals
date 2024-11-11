/*
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
binary search tree.

 

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.

*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode result = recursive(new TreeNode(), nums);
        return result;
    }

    public TreeNode recursive(TreeNode tn, int[] nums) {
        tn = new TreeNode(midElement(nums));
        if (nums.length >= 2) tn.left = recursive(new TreeNode(), Arrays.copyOfRange(nums, 0, midIndex(nums)));
        if (nums.length >= 3) tn.right = recursive(new TreeNode(), Arrays.copyOfRange(nums, midIndex(nums) + 1, nums.length));
        return tn;
    }

    public int midElement(int[] nums) {
        return nums[midIndex(nums)];
    }

    public int midIndex(int[] nums) {
        return (int) Math.ceil((nums.length - 1) / 2.0);
    }
}
