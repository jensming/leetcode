class Solution(object):
    def longestCommonPrefix(strs):
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        shortest = min(len(first),len(last))
        result = ""
        for i in range(shortest):
            if first[i] != last[i]:
                return result
            else:
                result += first[i]
        return result
                
# "fl" expected
strs = ["flower","flow","flight"]
print(Solution.longestCommonPrefix(strs))

# "" expected
strs = ["dog","racecar","car"]
print(Solution.longestCommonPrefix(strs))

# "sca" expected
strs = ["scar","scare","scab","scam"]
print(Solution.longestCommonPrefix(strs))