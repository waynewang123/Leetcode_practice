class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##如果能把二维矩阵转化为1纬数组就行
        if matrix is None or len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left,right = 0,row*col-1
        while left <= right:
            mid = left + (right-left)//2
            element = matrix[mid//col][mid%col]
            if element == target:
                return True
            elif element > target:
                right = mid -1
            else:
                left = mid + 1
        return False