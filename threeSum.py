class Solution(object):
    def threeSum(nums):
        nums = sorted(nums)
        result = []
        indx = 0
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]<0:
                    j += 1
                elif nums[j]+nums[k]+nums[i]>0:
                    k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==result[indx][1]:
                        j += 1
                    while j<k and nums[k]==result[indx][2]:
                        k -= 1
                    indx += 1
        return result
    
#[[-1,-1,2],[-1,0,1]] expected
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))

#[] expected
nums = [0,1,1]
print(Solution.threeSum(nums))

#[0,0,0] expected
nums = [0,0,0]
print(Solution.threeSum(nums))