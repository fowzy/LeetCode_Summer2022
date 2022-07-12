class Solution(object):
    def __init__(self):
        self.parenthesesStack = []
    ######
    # check is problem so if we send a closing from type ] 
    # we have to check if this [ exist in the stack
    ######
    def check(self, p):
        # case 1:
        # ] gets here
        # stack has (
        # so if the stack does not have [ we should return false 
        # case 2:
        # stack )
        if(p=="]" and len(self.parenthesesStack)!=0):
            if self.parenthesesStack[-1] == "[":
                return True
            else:
                return False
        if(p==")" and len(self.parenthesesStack)!=0):
            if self.parenthesesStack[-1] == "(":
                return True
            else:
                return False
        if(p=="}" and len(self.parenthesesStack)!=0):
            if self.parenthesesStack[-1] == "{":
                return True
            else:
                return False
        if len(self.parenthesesStack) == 0:
            return False

    def isValid(self, s):
        for i in range(0,len((s))):
            if s[i] == "(":
                self.parenthesesStack.append(s[i])
            if s[i] == ")":
                if(self.check(s[i])):
                    self.parenthesesStack.pop()
                else:
                    return False
            if s[i] == "[":
                self.parenthesesStack.append(s[i])
            if s[i] == "]":
                if(self.check(s[i])):
                    self.parenthesesStack.pop()
                else:
                    return False
            if s[i] == "{":
                self.parenthesesStack.append(s[i])
            if s[i] == "}":
                if(self.check(s[i])):
                    self.parenthesesStack.pop()
                else:
                    return False
        # Final decision
        if(len(self.parenthesesStack) == 0):
            return True
        else:
            return False

s0 = Solution()
s1 = Solution()
s2 = Solution()
s3 = Solution()
s4 = Solution()
s5 = Solution()

print(s0.isValid('([)]'))

print(s1.isValid('{[]}'))

print(s2.isValid('()'))

print(s3.isValid('()[]{}'))

print(s4.isValid('(]'))

print(s5.isValid(']'))
