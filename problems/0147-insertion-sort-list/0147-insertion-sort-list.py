class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = head

        while current is not None:
            next_node = current.next

            prev = dummy
            while prev.next is not None and prev.next.val < current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next