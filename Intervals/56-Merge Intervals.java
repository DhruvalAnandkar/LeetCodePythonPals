/*
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

*/
import java.util.*;
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Double.compare(a[0], b[0]));
        int i = 0;
        while (i < intervals.length - 1) {
            if (intervals[i][1] >= intervals[i + 1][0]) {
                intervals[i][1] = Math.max(intervals[i + 1][1], intervals[i][1]);
                intervals = removeElement(intervals, i + 1);
                i--;
            }
            i++;
        }      
        
        return intervals;
    }

    public int[][] removeElement(int[][] arr, int ind) {
        for (int i = ind; i < arr.length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr = Arrays.copyOfRange(arr, 0, arr.length - 1);
        return arr;
    }
    
}
