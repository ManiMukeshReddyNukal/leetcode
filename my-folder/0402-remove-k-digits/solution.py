class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digit in num:
            while k and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        finalstack=stack[:-k] if k else stack
        return "".join(finalstack).lstrip("0") or "0"
