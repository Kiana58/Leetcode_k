class TicTacToe:

    def __init__(self, n: int):
        # count from 0, if count == n, player 1 wins, if -n, player 2 wins
        self.rows=[0]*n
        self.cols=[0]*n
        # diagonal only X in the board satisfies
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        # although called move, but is for define who wins after the move
        n=self.n
        
        self.rows[row]+=1 if player==1 else -1
        self.cols[col]+=1 if player==1 else -1
        # for diagnal \
        if row-col==0: self.diag1+=1 if player==1 else -1
        # for diagonal /
        if row+col==n-1: self.diag2+=1 if player==1 else -1
            
        if self.rows[row]==n or self.cols[col]==n or self.diag1==n or self.diag2==n: return 1
        if self.rows[row]==-n or self.cols[col]==-n or self.diag1==-n or self.diag2==-n: return 2
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
