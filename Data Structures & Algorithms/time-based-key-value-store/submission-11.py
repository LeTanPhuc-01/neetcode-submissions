class TimeMap:

    def __init__(self):
        self.time_dict = {} #key = string, value = list of [value, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []
        self.time_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_dict.get(key, [])
        #binsearch
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r-l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
