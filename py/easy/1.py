# Problem LeetCode 1. Two Sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        seen = {}
        for i in range(length):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i
