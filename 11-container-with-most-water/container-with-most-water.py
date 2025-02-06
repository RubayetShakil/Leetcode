class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        maxi=0
        while i<j:
            if height[i]<height[j]:
                area=(j-i)*height[i]
                i+=1
            else:
                area=(j-i)*height[j]
                j-=1
            maxi=max(maxi,area)
        return maxi