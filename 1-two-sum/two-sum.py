class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        dict1={}
        i=0
        while True:
            dict1.update({nums[i]:i})
            i+=1
            if target-nums[i] in dict1.keys():
                lst.append(dict1[target-nums[i]])
                lst.append(i)
                break
        return lst


        
             



        