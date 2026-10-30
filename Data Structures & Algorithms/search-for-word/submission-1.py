class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if bord == []:
            return False 

        def dfs(r, c, index): 
            if index == len(word): 
                return True 
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False 

            currentChar = board[r][c]
            board[r][c] = "#"

            res = dfs(r-1, c, index + 1) or dfs(r+1, cindex + 1) or dfs(r, c+1, index + 1) or dfs(r, c-1, index + 1)
            board[r][c] = currentChar
            return res 

        for row in range(len(board)): 
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0): 
                        return True 

