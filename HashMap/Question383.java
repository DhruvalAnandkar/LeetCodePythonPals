/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
*/

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> map = new HashMap<>();
        char[] mag = magazine.toCharArray();
        char[] note = ransomNote.toCharArray();

        for(char c : mag){
            map.put(c, map.getOrDefault(c,0) + 1);
        }

        for(char c : note){
            if(!map.containsKey(c) || map.get(c) <=0)
                return false;
            map.put(c, map.get(c)-1);
        }
    return true;

    }
}
