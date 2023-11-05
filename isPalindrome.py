class Solution(object):
    def isPalindrome(x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
        
#True expected
num = "12521"
print(Solution.isPalindrome(num))

#False expected
num = "30"
print(Solution.isPalindrome(num))