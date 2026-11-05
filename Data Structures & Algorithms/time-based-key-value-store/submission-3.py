class TimeMap:
    def __init__(self):
        self.dict = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [[timestamp],[value]]
        else:
            self.dict[key][0].append(timestamp)
            self.dict[key][1].append(value)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        def keyIndex():
            timestamps = self.dict[key][0]

            if len(timestamps) < 2:
                if timestamps[0] <= timestamp:
                    return 0
                return ""

            l, r =  0, len(timestamps) - 1
            while l < r:
                m = (l + r) // 2

                if timestamps[m] == timestamp:
                    return m

                if r - l == 1:
                    if timestamp >= timestamps[r]:
                        return r
                    elif timestamp >= timestamps[l]:
                        return l
                    else:
                        return ""

                if timestamps[m] < timestamp:
                    l = m
                else:
                    r = m
            return key
        index = keyIndex()
        return self.dict[key][1][index] if isinstance(index, int) else ""