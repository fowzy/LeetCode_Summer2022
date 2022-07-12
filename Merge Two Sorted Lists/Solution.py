# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        n = ListNode()
        newList = []
        # newList = sorted(list1+list2)
        return newList

c0 = Solution()
print(c0.mergeTwoLists([1,2,4],[1,3,4]))
c1 = Solution()
print(c1.mergeTwoLists([],[]))
c2 = Solution()
print(c2.mergeTwoLists([],[0]))

