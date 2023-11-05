class Solution(object):
    def letterCombinations(digits):
        digits = str(digits)
        teleCode = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        if not digits:
            return []
        else:
            result = [""]
            for i in range(len(digits)):
                new_result = []
                for prev in result:
                    for letter in teleCode[digits[i]]:
                        new_result.append(prev+letter)
                result = new_result
            return result
        
#["ad","ae","af","bd","be","bf","cd","ce","cf"] expected
digits = 23
print(Solution.letterCombinations(digits))

#["p","q","r","s"] expected
digits = 7
print(Solution.letterCombinations(digits))