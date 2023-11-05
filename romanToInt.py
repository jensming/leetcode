class Solution(object):
    def romanToInt(s):
        romanNums = {'I':1,
                     'V':5,
                     'X':10,
                     'L':50,
                     'C':100,
                     'D':500,
                     'M':1000}
        result = 0
        for i in range(len(s)):
            if i>0 and romanNums[s[i]]>romanNums[s[i-1]]:
                result += romanNums[s[i]] - 2*romanNums[s[i-1]]
            else:
                result += romanNums[s[i]]
        return result
    
#58 expected
s = "LVIII"
print(Solution.romanToInt(s))

#1994 expected
s = "MCMXCIV"
print(Solution.romanToInt(s))