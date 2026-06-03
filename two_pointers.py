# Two Sum II (Given a sorted array, find two numbers that add up to a target).

def two_sum_sorted(arr, target):
	left = 0
	right = len(arr) - 1

	while left < right:
		current_sum = arr[left] + arr[right]

		if current_sum == target:
			return [left, right]
		elif current_sum < target:
			left += 1
		else:
			right -= 1

	return []

# Testing the Algorithm
if __name__ == "__main__":
	sorted_array = [1, 4, 5, 6, 7, 9, 11, 14, 18, 19, 23]
	target_value = 21

	result = two_sum_sorted(sorted_array, target_value)
	print(f"In the array: {sorted_array} values at index: {result} adds up to the target of {target_value}.")