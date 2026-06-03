# Maximum Sum Subarray of Size K.

def max_subarray_sum(arr, k):
	if len(arr) < k:
		return 0
	
	# Calculate the sum of the very first window
	window_sum = sum(arr[:k])
	max_sum = window_sum

	# Slide the window from left to right across the array
	for i in range(len(arr) - k):
		# Subtract the element leaving the back, add the element entering the front
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(max_sum, window_sum)
	
	return max_sum

# Testing the Algorithm
if __name__ == "__main__":
	test_array = [1, 3, 4, 12, 4, 5, 7, 11, 1, 3, 5]
	k_value = 4
	result = max_subarray_sum(test_array, k_value)
	print(f"Maximum sum of a subarray of length {k_value} in the array: {test_array} is {result}")