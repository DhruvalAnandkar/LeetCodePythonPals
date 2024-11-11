/*
https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

*/
class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> openers = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                openers.add(c);
            } else {
                if ((openers.size() >= 1) &&
                    ((c == ')' && openers.get(openers.size() - 1) == '(') ||
                    (c == ']' && openers.get(openers.size() - 1) == '[') ||
                    (c == '}' && openers.get(openers.size() - 1) == '{')))
                    openers.remove(openers.size() - 1);
                else
                    return false;
            }
        }
        return openers.size() == 0;
    }
}
