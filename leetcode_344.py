class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ##先用双指针左，交换左右的值，L++，r--，直到l>= r
        left = 0 
        right = len(s) -1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left = left + 1
            right = right - 1
        return s

#########################################################
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recursion(s,0,len(s)-1)
    def recursion(self,s,left,right):
        if left >= right:
            return
        self.recursion(s,left+1,right-1)
        s[left],s[right] = s[right],s[left]
