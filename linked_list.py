class Node:
	"""An individual unit of a Linked List."""
	def __init__(self, data):
		self.data = data
		self.next = None  # Pointer to the next node, defaults to None

class LinkedList:
	"""Wrapper class to manage node manipulation"""
	def __init__(self):
		self.head = None  # The entry point of the list
	
	def prepend(self, data):
		"""Insert a node at the very beginning: O(1) time."""
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	
	def append(self, data):
		"""Insert a node at the very end: O(n) time."""
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return

		current = self.head
		while current.next:
			current = current.next
		current.next = new_node

	def delete_by_value(self, value):
		"""Delete the first node containing the target value: O(n) time."""
		if not self.head:
			return
		
		# Case 1: The head node itself hodls the target
		if self.head.data == value:
			self.head = self.head.next
			return
		
		# Case 2: Traverse to find the node right BEFORE the target
		current = self.head
		while current.next and current.next.data != value:
			current = current.next
		
		# If found, bypass the target node
		if current.next:
			current.next = current.next.next
	
	def display(self):
		"""Traverse and print the list: O(n) time."""
		elements = []
		current = self.head
		while current:
			elements.append(str(current.data))
			current = current.next
		print(" -> ".join(elements) + " -> None")

def reverse_iterative(llist):
	"""Reverse a linked list in-place using iteration: O(n) Time, O(1) Space."""
	prev = None
	current = llist.head

	while current:
		next_node = current.next	# Step 1: Save the remaining list
		current.next = prev				# Step 2: Reverse the pointer direction
		prev = current						# Step 3: Shift 'prev' forward
		current = next_node				# Step 4: Shift 'current' forward
	
	llist.head = prev  # Reset the head to the next front of the list

def reverse_recursive_helper(node):
	"""Recursive helper function that returns the new head."""
	if not node or not node.next:
		return node  # Base case: empty list or single node is already reversed
	
	new_head = reverse_recursive_helper(node.next)

	# flip the link: Make the next node point back to the current node
	node.next.next = node
	node.next = None  # Clear out the original forward pointer to avoid cycles
	return new_head

def reverse_recursive(llist):
	"""Reverses the linked list in-place using recursion: O(n) Time, O(n) Space."""
	llist.head = reverse_recursive_helper(llist.head)

def has_cycle(llist):
	"""Detects loops in a linked list using two pointers."""
	slow = llist.head
	fast = llist.head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			return True
	
	return False

# Test
if __name__ == "__main__":
	linked_list = LinkedList()

	linked_list.append(2)
	linked_list.append(4)
	linked_list.append(23)

	linked_list.prepend(12)
	linked_list.prepend(6)
	linked_list.prepend(8)

	linked_list.display()

	linked_list.delete_by_value(4)

	linked_list.display()

	reverse_iterative(linked_list)

	linked_list.display()
	