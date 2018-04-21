import string
class Solution:
    def plusOne(self, digits):
        str1=''
        for a in digits:
            str1 = str1+(str(a))
        num=int(str1)
        num=num+1
        str2=str(num)
        list2=list(str2)
        list3=[]
        for b in list2:
            b=int(b)
            list3.append(b)
        return  list3

print(Solution.plusOne(0,[1,2]))
