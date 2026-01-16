class Solution:
    def letterCombinations(self, digits: str):
        combination = []
        dic = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["s","t","u"],
            "9" : ["w","x","y","z"]
        }
        if len(digits) == 1 and digits[0] in dic.keys():
            return dic[digits[0]]

        for i in digits:
            if i in dic.keys():
                pass

