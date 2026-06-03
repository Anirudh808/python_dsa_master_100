class DLLNode:
	def __init__(self, data):
		self.data = data
		self.prev = None  # Pointer to the previous node
		self.next = None  # Pointer to the next node

# The Structural Trade-off

# The Good: You can now traverse the list in both directions. Deleting a node is cleaner because you no longer need to track a separate "previous" explorer variable—the node itself already holds a link to its neighbor behind it!

# The Catch: Every insertion and deletion requires managing four pointers instead of two to keep the chain synchronized. It also consumes slightly more memory per node to store that extra reference.

# Circular linked list.
# A circular linked list can be singly or double linked. The only thing here is the .next pointer of the very last node does not point to none, instead it points directly to the head node.

# Finding the middle of the linked list.
def find_middle(head):
	slow = head
	fast = head

	# Fast moves two steps, slow moves one step
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	# When the fast finishes, slow is right at the midpoint.
	return slow

# Merging two sorted lists
# Take two sorted linked lists and splice them together into a single sorted list.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
def merge_two_lists(l1, l2):
	# Create a placeholder dummy node to anchor our new track
	dummy = Node(0)
	current = dummy

	# Compare heads of both lists and stich the smaller one
	while l1 and l2:
		if l1.data <= l2.data:
			current.next = l1
			l1 = l1.next
		else:
			current.next = l2
			l2 = l2.next
		current = current.next
	
	# Cleanup Crew: Append whichever list still has elements remaining
	current.next = l1 if l1 else l2
	
	return dummy.next  # Return the real head (right after the dummy)


def delete_node_in_dll(target):
	"""Bypassses the target node in a Doubly Linked List."""
	if not target:
		return
	
	# Link the node behind target to the node in front of the target
	if target.prev:
		target.prev.next = target.next

	# Link the node in front of the target back to the node behind target
	if target.next:
		target.next.prev = target.prev
	