

class Solution:
    def isHappy(self, n: int) -> bool:
        check = False
        while True:
            numbers = []
            while n > 0:
                numbers.append(n % 10)
                n //= 10

            if len(numbers) == 1 and numbers[0] != 1:
                if numbers[0] ** 2 < 10 or check:
                    return False
                check = True
            elif len(numbers) == 1 and numbers[0] == 1:
                return True
            n = 0
            for num in numbers:

                n += (num ** 2)


n = 2
print(Solution().isHappy(n=n, ))
