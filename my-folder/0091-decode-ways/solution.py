class Solution:
    def numDecodings(self, s: str) -> int:
        dp={len(s):1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            resp=dfs(i+1)
            if (i+1<len(s) and (s[i]=="1" or ( s[i]=="2" and s[i+1] in "0123456"))):
                resp+=dfs(i+2)
            dp[i]=resp
            return resp
        return dfs(0)
