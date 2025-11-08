# 给你一个链表，删除聊表的倒数第n个结点，并且返回料边的头结点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        right = dummy
        for _ in range(n):
            right = right.next
        
        left = dummy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next