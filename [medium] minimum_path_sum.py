# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for x in range(1, len(grid) + len(grid[0])):
            for y in range(x + 1):
                i = y
                j = x - y
                if i < len(grid) and j < len(grid[0]):
                    if i == 0:
                        grid[i][j] = grid[i][j] + grid[i][j - 1]
                    elif j == 0:
                        grid[i][j] = grid[i][j] + grid[i - 1][j]
                    else:
                        grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i - 1][j])
        
        return grid[len(grid) - 1][len(grid[0]) - 1]
