# 给定一个链表的头结点head，返回链表开始入环的第一个节点。
# 如果链表无环，则返回null。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slot is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None