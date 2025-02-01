class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[0]
        sum=0
        for i in gain:
            
            sum+=i
            alt.append(sum)


        max=0
        for i in alt:
            if i>max:
                max=i
        return max