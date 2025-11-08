# 有一个单链表的head，我们想删除它其中的一个节点node.
# 给你一个需要删除的节点node。你将无法访问第一个节点head。
# 链表中的每个节点都有一个唯一的值。并且保证给定的节点node不是链表中的最后一个节点。
# 删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
# 1. 给定节点的值不应该存在于链表中
# 2. 链表中的节点数应该减少1
# 3. node前面的所有值顺序相同
# 4. node后面的所有值顺序相同

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 时间复杂度：0(1)，空间复杂度：0(1)
    def deleteNode(self, node: ListNode) -> None:
        # 因为无法访问头节点，所以只能把下一个节点的值覆盖到当前节点
        node.val = node.next.val
        node.next = node.next.next
