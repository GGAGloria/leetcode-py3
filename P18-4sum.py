class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range (n-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            j = i + 1
            k = n-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s<target:
                    j = j+1
                elif s>target:
                    k = k-1
                else:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    result.append(temp)
                    j = j+1
                    k = k-1
                    while j<k and nums[j]==nums[j-1]:
                        j = j+1
                    while j<k and nums[k]==nums[k+1]:
                        k = k-1
        return result
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        if len(nums) == 0:
            return result
        if target>nums[-1]*4:
            return result
        for i in range(len(nums)):
            if target<nums[i]*4:
                return result
            if i==0 or (i>0 and nums[i-1]!=nums[i]):
                res = self.threeSum(nums[i+1:],(target-nums[i]))
                if len(res) != 0:
                    for a in res:
                        temp = [nums[i]]+a
                        result.append(temp)
        return result
        
        
        