from _ast import List

nums = [1, 3, 5, 6]
target = 2


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1

        while left_pointer <= right_pointer:
            pivot = left_pointer + (right_pointer - left_pointer) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right_pointer = pivot - 1
            else:
                left_pointer = pivot + 1

        return left_pointer


# Driver Code
insert_position = Solution().searchInsert(nums, target)
print(insert_position)