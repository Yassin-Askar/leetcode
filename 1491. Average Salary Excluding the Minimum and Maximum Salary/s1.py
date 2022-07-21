class Solution:
    def average(self, salary: list[int]) -> float:
        maxs = max(salary)
        mins = min(salary)
        return (sum(salary)-maxs-mins) / (len(salary)-2)
