class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r=""
        l=100000
        for i in strs:
            if l > len(str(i)):
               l=len(i)
               r = i
        jz = l
        for j in range(l):
            for w in strs:
                if r[j]!=w[j]:
                    return r[0:j]

        return r


print(Solution.longestCommonPrefix(0,["asdabc","asd"]))
