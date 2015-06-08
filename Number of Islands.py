# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        """
        DFS or BFS
        """
        count = 0
        if len(grid) == 0 or grid == None:
            return 0

        for i, t in enumerate(grid):
            for j, val in enumerate(t):
                if val == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count


    def dfs(self, grid, i, j):
        grid[i][j] = '0'

        if i > 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if i < len(grid) -1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)
        if j < len(grid[0]) -1 and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)


s = Solution()
island = [
    ['1', '1', '0', '0', '0'], 
    ['1', '1', '0', '0', '0'], 
    ['0', '0', '1', '0', '0'], 
    ['0', '0', '0', '1', '1']
]
print s.numIslands(island)
