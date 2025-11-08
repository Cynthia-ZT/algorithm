# 给定一个已排序的链表的头head，删除原始链表中所有重复数字的节点，值留下不同的数字。返回已排序的链表。
# 跟83的不同是，只要有重复出现过的都删掉，比如1,2,2,3要变成1,3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 时间复杂度：0(n)，空间复杂度：0(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val = val:
                while cur.next and cur.next.next = val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next