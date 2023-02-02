class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = {}
        for course in prerequisites:
            if course[0] not in courses:
                courses[course[0]] = [course[1]]
            else:
                courses[course[0]] += [course[1]]
        print(courses)
        for course in courses:
            if c in courses[course]:
                if course in courses[c]:
                    return False
        return True


print(Solution().canFinish(2, [[1, 0]]))
