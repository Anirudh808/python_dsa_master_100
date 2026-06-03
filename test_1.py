# 1) Problem: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with $O(\log n)$ runtime complexity.

def problem1(arr, target):
	low = 0
	high = len(arr) - 1
	mid = (low + high) // 2

	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	
	return low

nums = [1, 3, 5, 6]
print(problem1(nums, 2))

# Problem 2: Segregate Zeros and Ones (Two Pointers)Problem: Given an array containing only 0s and 1s, sort the array in-place in a single pass. You cannot use Python's built-in .sort() or count the number of zeros and ones. Your time complexity must be $O(n)$ and space complexity must be $O(1)$.

def problem2(arr):
	write_ptr = 0

	for read_ptr in range(len(arr)):
		if arr[read_ptr] == 0:
			arr[write_ptr], arr[read_ptr] = arr[read_ptr], arr[write_ptr]
			write_ptr += 1
	
	return arr

nums = [1, 0, 1, 1, 0, 0, 1]
problem2(nums)
print(nums)
