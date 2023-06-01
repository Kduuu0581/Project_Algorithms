from typing import List


def find_duplicate(nums: List[int]) -> int:
    if not nums:
        return False
    nums.sort()

    for i in range(len(nums) - 1):
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
