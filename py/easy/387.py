# Problem LeetCode 387. First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for i, item in enumerate(s):
            if item in char:
                char[item] = (i, char[item][1] + 1)
            else:
                char[item] = (i, 1)

        for index, count in char.values():
            if count < 2:
                return index

        return -1
