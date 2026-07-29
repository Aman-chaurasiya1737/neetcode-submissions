class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i in range(len(board[0])):
            s=set()
            for j in range(len(board)):
                if board[i][j].isdigit() and board[i][j] in s:
                    return False
                elif board[i][j].isdigit():
                    s.add(board[i][j])
        for i in range(len(board[0])):
            s=set()
            for j in range(len(board)):
                if board[j][i].isdigit() and board[j][i] in s:
                    return False
                elif board[j][i].isdigit():
                    s.add(board[j][i])
        for i in a:
            s=set()
            for j in range(i[0],i[0]+3):
                for k in range(i[1],i[1]+3):
                    if board[j][k].isdigit() and board[j][k] in s:
                        return False
                    elif board[j][k].isdigit():
                        s.add(board[j][k])
        return True
        