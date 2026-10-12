class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for num in tokens:
            if num == "+":
                q.append(q.pop() + q.pop())
            elif num == "-":
                a, b = q.pop(), q.pop()
                q.append(b - a)
            elif num == "*":
                q.append(q.pop() * q.pop())
            elif num == "/":
                a, b = q.pop(), q.pop()
                q.append(int(float(b) / a))
            else:
                q.append(int(num))
        return q[0]