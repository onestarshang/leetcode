"""
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        last = head
        current = head.next
        while current:
            if current.val == last.val:
                last.next = current.next
            else:
                last = current
            current = current.next
        return head


if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3

    p = s.deleteDuplicates(n1)
    assert n1.val == 1
    assert n1.next.val == 2
