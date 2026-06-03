def merge_sort(arr):
	# Base case: If the array has 1 or 0 elements, it's already sorted.
	if len(arr) <= 1:
		return arr
	
	# 1. DIVIDE: Find the midpoint and split the array in half.
	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]

	# Recursively sort both halves
	merge_sort(left_half)
	merge_sort(right_half)

	# 2. CONQUER: Merge the two sorted halves back into the original array
	i = 0  # Pointer for left_half
	j = 0  # Pointer for right_half
	k = 0  # Pointer for the main arr

	# Compare elements from both halves and copy the smaller one
	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			arr[k] = left_half[i]
			i += 1
		else:
			arr[k] = right_half[j]
			j += 1
		k += 1
	
	# If any elements are left over in left_half, copy then
	while i < len(left_half):
		arr[k] = left_half[i]
		i += 1
		k += 1
	
	# If any elements are left over in right_half, copy then
	while j < len(right_half):
		arr[k] = right_half[j]
		j += 1
		k += 1

def merge_sort_self(arr):
	if len(arr) <= 1:
		return arr
	
	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]

	merge_sort_self(left_half)
	merge_sort_self(right_half)

	i = j = k = 0

	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			arr[k] = left_half[i]
			i += 1
		else:
			arr[k] = right_half[j]
			j += 1
		k += 1
	
	while i < len(left_half):
		arr[k] = left_half[i]
		i += 1
		k += 1
	
	while j < len(right_half):
		arr[k] = right_half[j]
		j += 1
		k += 1

# --- Testing the Algorithm ---
if __name__ == "__main__":
	test_array = [38, 27, 43, 3, 9, 82, 19, 10]
	print(f"Original Array: {test_array}")

	merge_sort_self(test_array)

	print(f"Soted array: {test_array}")