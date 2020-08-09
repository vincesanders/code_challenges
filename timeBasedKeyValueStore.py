'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)
    - Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)
    - Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
    - If there are multiple such values, it returns the one with the largest timestamp_prev.
    - If there are no values, it returns the empty string ("").
'''
import math
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.store is a dictionary it's values are dictionaries key = timestamp value = value
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][timestamp] = value
        else:
            self.store[key] = {}
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        output = ('', -math.inf)
        if key in self.store:
            while timestamp > 0:
                if timestamp in self.store[key]:
                    return self.store[key][timestamp]
                else:
                    # if we don't have a matching timestamp key in the dict
                    # keep walking the timestamp back till we find a matching key
                    timestamp -= 1
        
        return output[0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)