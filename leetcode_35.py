class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1

        #print(mid,nums[mid])

        if nums[mid] > target: #注意，是target替换nums[mid]的位置
            return mid

        return mid + 1
