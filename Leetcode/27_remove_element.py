class Solution:
    def removeElement(self, nums:list(int), val: int) -> int:
            nums_len = len(nums)
            arr = [k for k in nums if k != val]
            for i in range(nums_len-len(arr)):
                arr.append('_')
            return len(arr)