class Solution(object):
    def removeDuplicates(nums):
        i = 1
        while i < len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
# 2 expected
lst = [1,1,2]
print(Solution.removeDuplicates(lst))

# 5 expected
lst = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(lst))