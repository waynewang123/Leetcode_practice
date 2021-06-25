class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##左右两个指针，l,r,mid = l+r/2
        ## 如果muns[mid] < target:l = mid + 1
        ##如果nums[mid] > target:r = mid - 1
        if nums is None or len(nums) == 0:
            return -1
        l = 0 
        r = len(nums) -1
        while (l<=r):
            mid = int((l+r)/2)
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                return mid
        return -1