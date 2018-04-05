class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        for i in nums:
            if i not in new:
                new.append(i)
        nums = new
        return len(new)
print(Solution.removeDuplicates(0,[1,1,1,1,2]))
