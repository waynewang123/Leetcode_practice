class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ##救生艇，双指针
        ##先排序，如果最大+最小可以一起走，那都可以走
        ##corner case
        if people is None or len(people) == 0:
            return 0
        people.sort()##升序
        i = 0
        j = len(people) - 1
        res = 0
        while i < = j:
            if people[i] + people[j] <= limit:
                i = i + 1
            j = j -  1
            res = res + 1
        return res

