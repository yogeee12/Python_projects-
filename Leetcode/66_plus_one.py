class Solution:
    def plusOne(self, digits):
        strs = ''
        for i in digits:
            strs += str(i)
        strs = int(strs)+1
        strs = str(strs)
        digits = []
        for k in strs:
            digits.append(int(k))
        return digits
s1 = Solution()
print(s1.plusOne([1,2,9]))