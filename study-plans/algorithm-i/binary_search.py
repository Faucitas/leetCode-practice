from typing import List

nums = [-1,0,3,5,9,12]
target = 2


def search(nums: List[int], target: int):
    left_pointer, right_pointer = 0, len(nums) - 1
    while left_pointer <= right_pointer:
        pivot = left_pointer + (right_pointer - left_pointer) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right_pointer = pivot - 1
        else:
            left_pointer = pivot + 1
    return -1


# Driver Code
num_index = search(nums, target)
print(num_index)