class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        capacity = 0
        while r >= l:
            capacity = people[r]
            r -= 1
            capacity += people[l]
            boats += 1
            if capacity <= limit:
                l += 1
        return boats


people = [1, 2]
limit = 3
print(Solution(). numRescueBoats(people=people, limit=limit, ))
