/*
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

*/

class Solution {
    public boolean isValidSudoku(char[][] board) {
        //rows
        for (int i = 0; i < 9; i++) {
            boolean[] checks = {false, false, false, false, false, false, false, false, false};
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int curr = Character.getNumericValue(board[i][j]);
                if (!checks[curr - 1]) {
                    checks[curr - 1] = true;
                } else {
                    return false;
                }
            }
         }

         //columns
         for (int i = 0; i < 9; i++) {
            boolean[] checks = {false, false, false, false, false, false, false, false, false};
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                int curr = Character.getNumericValue(board[j][i]);
                if (!checks[curr - 1]) {
                    checks[curr - 1] = true;
                } else {
                    return false;
                }
            }
         }

         //3x3 squares
         int jOffset = 0;
         boolean[] checks = {false, false, false, false, false, false, false, false, false};
         for (int i = 0; i < 27; i++) {
            if (i == 9 || i == 18) jOffset += 3; //permanently move down by 3 when the 1st or 2nd set of 3 boxes are done
            if (i % 3 == 0) Arrays.fill(checks, false); //reset checks when moving to next box
            for (int j = 0; j < 3; j++) {
                if (board[i % 9][j + jOffset] == '.') continue;
                int curr = Character.getNumericValue(board[i % 9][j + jOffset]);
                if (!checks[curr - 1]) {
                    checks[curr - 1] = true;
                } else {
                    return false;
                }
            }
         }
        return true;
    }
}
