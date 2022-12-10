class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [[value, timestamp]]
        else:
            self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        if key not in self.time_map:
            return ""

        right = len(self.time_map[key]) - 1
        res = ""
        while left <= right:
            mid = (left+right)//2
            if timestamp >= self.time_map[key][mid][1]:
                res = self.time_map[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
