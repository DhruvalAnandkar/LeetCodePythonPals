/*
https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=greedy

409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
*/


//WIP, not working
import java.util.*;
class Solution {
        public int longestPalindrome(String s) {
        String[] arr = s.split("");
        arr = Arrays.copyOfRange(arr, 1, arr.length);
        Arrays.sort(arr);
        boolean hasOdd = false;
        int k = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == arr[i - 1]) {
                k++;
                i++;
            } else {
                hasOdd = true;
            }
        }
        return (hasOdd) ? (k * 2) + 1 : k * 2;
    }
}
