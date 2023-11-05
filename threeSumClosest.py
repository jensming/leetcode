class Solution(object):
    def threeSumClosest(nums, target):
        nums = sorted(nums)
        closestSum = 0
        threeSum = 0
        diff = 0
        minDiff = 10E4  #assuming -10E4 <= target <= 10E4
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while j<k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum==target:
                    return threeSum
                elif threeSum<target:
                    j += 1
                elif threeSum>target:
                    k -= 1
                diff = abs(threeSum-target)
                if diff<minDiff:
                    minDiff = diff
                    closestSum = threeSum
        return closestSum
    
# 2 expected
nums = [-1,2,1,-4]
target = 1
print(Solution.threeSumClosest(nums,target))

# 4 expected
nums = [3,-2,3,1,0]
target = 5
print(Solution.threeSumClosest(nums,target))