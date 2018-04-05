class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=Stack()
        s2=Stack()
        for i in s:
            st.push(i)
        for i in s:
            if st.peek()=='}' or st.peek()==']' or st.peek()== ')':
                s2.push(st.pop())
            else:
                if st.peek()=='(':
                    if s2.peek()!=')':
                        return False
                    else:
                        st.pop()
                        s2.pop()
                if st.peek()=='[':
                    if s2.peek()!=']':
                        return False
                    else:
                        st.pop()
                        s2.pop()
                if st.peek()=='{':
                    if s2.peek()!='}':
                        return False
                    else:
                        st.pop()
                        s2.pop()
        if st.isEmpty() and s2.isEmpty():
            return True
        else:
            return False


print(Solution.isValid(0 , '(}'))
