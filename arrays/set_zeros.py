class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # https://leetcode.com/problems/set-matrix-zeroes/
        
        # Approach 1: Hash set and O(m+n) space
#         row_set = set()
#         col_set = set()
        
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == 0:
#                     row_set.add(row) 
#                     col_set.add(col)
                    
        
                
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if row in row_set or col in col_set:
#                     matrix[row][col] = 0

        # Approach 2. Consider the first row and column as flags. 
        # since 0,0 overlap with row and column, have a flag for column = 0
        column = 1
                    
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    
                    if col == 0:
                        column = 0
                    else:
                        matrix[0][col] = 0
                        
        print(matrix)
                    
                        
        for row in range(len(matrix)-1, -1, -1):
            for col in range(len(matrix[0])-1, -1, -1):
                if matrix[row][col] != 0:
                    if col != 0: 
                        if matrix[row][0] == 0 or matrix[0][col] == 0:
                            matrix[row][col] = 0
                    else:
                        if column == 0 or matrix[row][0] == 0:
                            matrix[row][col] = 0