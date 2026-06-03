def binary_search(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		# Find the exact middle index
		mid = (low + high) // 2

		# Scenario 1: We found the target! Return it's index.
		if arr[mid] == target:
			return mid
		
		# Scenario 2: The middle value is too big.
		# Throw away the right half by shifting the 'high' boundary.
		elif arr[mid] > target:
			high = mid - 1

		# Scenario 3: The middle value is too small.
		# Throw away the left half by shifting the 'low' boundary.
		else:
			low = mid + 1
	
	return -1

# --- Testing the Algorithm ---
sorted_numbers = [3, 9, 10, 27, 38, 43, 82]
target_value = 43

result = binary_search(sorted_numbers, target_value)
print(f"Target {target_value} found at index: {result}.")