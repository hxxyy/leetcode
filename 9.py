#Palindrome Number
import  math
class Solution:
    def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if 0<=x and x<=9:
            return True
        rtype=True
        s=str(x)
        num= len(s)
        s1= s[0:math.ceil(num / 2)]
        s2=s[math.floor(num/2):]
       # print(math.ceil(num/2))
        for i in range(math.ceil(num/2)):
            if s1[i] != s2[math.ceil(num/2)-1-i]:
                rtype = False
        return rtype



print(Solution.isPalindrome(0,10))

