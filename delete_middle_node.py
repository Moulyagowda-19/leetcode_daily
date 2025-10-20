def deleteMiddle(self, head):
        if not head or not head.next:
            return None  # Only one node

        slow = head
        fast = head
        prev = None

    # Find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

    # Delete the middle node
        prev.next = slow.next

        return head
