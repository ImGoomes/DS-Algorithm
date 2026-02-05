# Problem LeetCode 218. Contains Duplicate II - Slinding Window Alternative (space-efficient when k is small relative to n)


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    window = set()

    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])

    return False
