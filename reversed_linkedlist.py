def reverseList(self, head):
        prev = None
        current = head
        head = prev
        while current is not None:
            n = current.next
            current.next= prev
            prev=current
            current = n
        return prev