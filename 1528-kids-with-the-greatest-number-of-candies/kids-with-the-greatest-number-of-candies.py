class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=0
        lst=[]
        for i in candies:
            if i>max:
                max=i
        for i in candies:
            if extraCandies+i>=max:
                lst.append(True)
            else:
                lst.append(False)
        return lst
