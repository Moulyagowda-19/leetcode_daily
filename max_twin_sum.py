def pairSum(self, head):
        # Step 1: Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compute twin sums
        max_sum = 0
        first, second = head, prev
        while second:  # only need to traverse half
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum
