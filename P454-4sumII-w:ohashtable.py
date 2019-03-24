class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range (n-2):
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
                    if nums[j+1]==nums[j] and nums[k-1]!=nums[k]:
                        j = j+1
                    elif nums[j+1]==nums[j] and nums[k-1]==nums[k]:
                        j = j+1
                    elif nums[j+1]!=nums[j] and nums[k-1]==nums[k]:
                        k = k+1
                    else:
                        j = j+1
                        k = k-1
        return result
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count = 0
        if len(nums) == 0:
            return 0
        if target>nums[-1]*4:
            return 0
        for i in range(len(nums)):
            if target<nums[i]*4:
                return count

            res = self.threeSum(nums[i+1:],(target-nums[i]))
            if len(res) != 0:
                for a in res:
                    print(str(nums[i])+" "),
                    print(a)
                    count += 1
        return count
        
        
        
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        E = [100*x+1 for x in A]
        F = [100*x+2 for x in B]
        G = [100*x+4 for x in C]
        H = [100*x-7 for x in D]
        nums = E+F+G+H
        return self.fourSum(nums,0)
        
        