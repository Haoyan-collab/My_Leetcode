from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

        # key -> list(value, timestamp)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        lst = self.mp[key]
        n = len(lst)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right)//2
            val, time = lst[mid]
            if time <= timestamp:
                left = mid + 1
            else:
                right =  mid - 1
        if left == 0:
            return ""
        val,_ = lst[left-1]
        return val

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)