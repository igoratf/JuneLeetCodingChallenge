class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        current = node
        while current.next:
            current.val = current.next.val
            if not current.next.next:
                current.next = None
            else:
                current = current.next
            