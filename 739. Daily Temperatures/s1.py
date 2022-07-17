
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = (i - stack_index)
            stack.append([temp, i])
        return result


temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]

print(Solution().dailyTemperatures(temperatures))
