class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operands = "+-/*"

        for i in tokens:
            if i not in operands:
                stk.append(i)
            else:
                val1 = int(stk.pop())
                val2 = int(stk.pop())
                if i == '+':
                    val = val2 + val1
                elif i == '-':
                    val = val2 - val1
                elif i == '/':
                    val = int(val2 / val1)
                elif i == '*':
                    val = val2 * val1
                stk.append(str(val))
        return int(stk.pop())
