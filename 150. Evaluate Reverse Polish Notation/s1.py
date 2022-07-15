

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "*": self.multiply,
            "+": self.sum,
            "-": self.subtraction,
            "/": self.division,

        }
        result = []
        for token in tokens:
            if token not in operations.keys():
                result.append(token)
            else:
                print((token))
                num2 = int(result.pop())
                num1 = int(result.pop())
                op = operations[token](num1, num2)
                result.append(op)

        return result[0]

    def multiply(self, x, y):
        return x * y

    def sum(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def division(self, x, y):
        return int(x / y)


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution().evalRPN(tokens=tokens))
