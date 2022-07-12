# Definition for singly-linked list.
from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        pass
c0 = Solution()
print(c0.mergeTwoLists([1,2,4],[1,3,4]))
# should return [1,1,2,3,4,4]
c1 = Solution()
print(c1.mergeTwoLists([],[]))
# should return []
c2 = Solution()
print(c2.mergeTwoLists([],[0]))
# should return [0]

