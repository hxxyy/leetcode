#other's
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

print(Solution.removeElement(0,[0,4,4,0,4,4,4,0,2],4))
