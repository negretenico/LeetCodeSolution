from typing import List


def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def backtracking(closed:int,opened:int, s:str):
        if closed == n and opened == n:
            ans.append(s)
            return
        if opened< n:
            backtracking(closed,opened+1,s+"(")
        if closed < opened:
            backtracking(closed+1,opened,s+")")
    backtracking(0,0,"")
    return ans
