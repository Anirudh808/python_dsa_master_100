def partition(arr, low, high):
	# We choose the rightmost element as our pivot
	pivot = arr[high]

	# 'i' tracks the boundary of elements smaller than the pivot
	# It starts just outside our current window
	i = low - 1

	# 'j' is the explorer traversing the array
	for j in range(low, high):
		# If the explorer finds an element smaller than the pivot...
		if arr[j] <= pivot:
			# ...we expand our "smaller elements boundary"
			i += 1
			# ...and swap the current element into that boundary
			arr[i], arr[j] = arr[j], arr[i]
	
	# Once the explorer finishes, we swap the pivot itself
	# to sit exactly right after our boundary of smaller elements.
	arr[i + 1], arr[high] = arr[high], arr[i + 1]

	# Return the final resting index of the pivot
	return i + 1

def quick_sort(arr, low, high):
	# Base case: if low is >= high, the array (or subarray) has 1 or 0 elements
	if low < high:
		# Partition the array and get the pivot's sorted index
		pi = partition(arr, low, high)

		# Recursively sort the left half (elements smaller than pivot)
		quick_sort(arr, low, pi - 1)

		# Recursively sort the right half (elements greater than pivot)
		quick_sort(arr, pi + 1, high)
	


def partition_self(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def quick_sort_self(arr, low, high):
	if low < high: 
		pi = partition_self(arr, low, high)
		quick_sort_self(arr, low, pi - 1)
		quick_sort_self(arr, pi + 1, high)

# --- Testing the Algorithm ---
if __name__ == "__main__":
	test_array = [10, 80, 30, 90, 40, 50, 70]
	print(f"Original array: {test_array}")

	# low is 0, high is the last index (length - 1)
	quick_sort_self(test_array, 0, len(test_array) - 1)

	print(f"Sorted array: {test_array}")