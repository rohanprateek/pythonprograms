# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:44:36 2021

@author: rohan
"""

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):

        filled = dict()
        for i in range(9):
            filled['row' + str(i)] = set()
            filled['col' + str(i)] = set()

        for i in range(9):
            for j in range(9):
                if A[i][j] != '.':
                    if A[i][j] not in filled['row' + str(i)]:
                        filled['row' + str(i)].add(A[i][j])
                    else:
                        return 0
                    if A[i][j] not in filled['col' + str(j)]:
                        filled['col' + str(j)].add(A[i][j])
                    else:
                        return 0
        
        box = 0
        row = 0
        col = 0

        while box != 9:
            box += 1
            filled['box' + str(box)] = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if A[i][j] != '.':
                        if A[i][j] not in filled['box' + str(box)]:
                            filled['box' + str(box)].add(A[i][j])
                        else:
                            return 0
            if box % 3 == 0:
                row = 0
                col += 3
            
            else:
                row += 3
        return 1

s = Solution()
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print(s.isValidSudoku(A))