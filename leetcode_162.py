class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        left,right = 0, len(nums)-1
        #如果中间值比右边大，说明峰值在左边，那就把right设置为mid
        while left<right:
            mid = left + (right - left)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
            return left
        