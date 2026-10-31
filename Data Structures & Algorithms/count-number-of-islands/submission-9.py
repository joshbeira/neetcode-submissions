class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []: 
            return 0

        def dfs(row, col): 
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] != "1": 
                return  

            grid[row][col] = "#"

            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1 , col)
            dfs(row-1, col)


        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):  
                if grid[i][j] == "1": 
                    dfs(i, j)
                    res += 1

        return res