class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {0: front}

        # Calculate the prefix sum for each node and add to the hashmap
        # Duplicate prefix sum values will be replaced
        while current is not None:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        # Reset prefix sum and current
        prefix_sum = 0
        current = front

        # Delete zero sum consecutive sequences 
        # by setting node before sequence to node after
        while current is not None:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return front.next
