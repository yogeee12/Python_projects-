class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_li = s.split(" ")
        s_li = [i for i in s_li if i != ""]
        print(s_li)
        return len(s_li[-1])

s1 = Solution()
print(s1.lengthOfLastWord("hello wolld   "))