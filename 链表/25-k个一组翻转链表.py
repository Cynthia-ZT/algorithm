# 给你链表的头结点head，每k个节点一组进行翻转，请你返回翻转后的链表。
# k是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单穿的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        dummy = ListNode(next=head)
        pre = None
        p0 = dummy
        cur = head
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
        
