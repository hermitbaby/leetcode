# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        """
        check row, column, block
        """
        # check each row
        for row in xrange(9):
            r_set = set()
            for val in board[row]:
                if val == '.':
                    continue
                if val not in r_set:
                    r_set.add(val)
                else:
                    return False

        # check each col
        for col in xrange(9):
            c_set = set()
            for row in xrange(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val not in c_set:
                    c_set.add(val)
                else:
                    return False

        # check each block
        for iBlock in xrange(3):
            for jBlock in xrange(3):
                b_set = set()
                for i in xrange(3):
                    for j in xrange(3):
                        val = board[iBlock*3 + i][jBlock*3 + j]
                        if val == '.':
                            continue
                        if val not in b_set:
                            b_set.add(val)
                        else:
                            return False

        return True
