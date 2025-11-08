# 给定一个单链表L的头结点head，单链表L表示为：
# L0 → L1 → … → Ln-1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 翻转后半段链表
    # 结合找中间节点和反转链表两题，得到两段链表，一段的head为head1，另一段head为head2
    # 然后合并两段链表，每次循环的时候，head1指向head2，head2指向head1.next 
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def reorderList(self, head: ListNode) -> None:
        def reverseList(head: ListNode) -> ListNode:
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        def middleNode(head: ListNode) -> ListNode:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = middleNode(head)
        head2 = reverseList(mid)
        head1 = head
        while head2:
            head1_nxt = head1.next
            head2_nxt = head2.next
            head1.next = head2
            head2.next = head1.next_nxt
            head1 = head1_nxt
            head2 = head2_nxt
    