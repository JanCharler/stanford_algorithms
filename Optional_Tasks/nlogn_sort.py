'''
An implementation of merge sort. Also counts inversions without almost no
added time.
'''

inversion = 0

def merge(arr1, arr2):
	'''
	Takes in 2 sorted arrays and merges them
	'''

	global inversion

	n = max(len(arr1), len(arr2))
	C = [None]*(len(arr1) + len(arr2))
	i =0
	j=0

	for k in range(len(C)):

		# End case
		if i >= len(arr1):
			C[k] = arr2[j]
			j+=1
			continue
		elif j >= len(arr2):
			C[k] = arr1[i]
			i+=1
			continue

		# Sorting
		if arr1[i] <= arr2[j]:		
			C[k] = arr1[i]
			i+=1
		elif arr2[j] <= arr1[i] or i >= len(arr1):
			C[k] = arr2[j]
			j+=1	

			# Inversion counter

			# Element of second array is added
			# Add to counter the amount of elements remaining in first array
			inversion += len(arr1)-i
			print(f"arr: {arr1,arr2} , i: {i} j: {j}")
			print(f"Inversion. Val: {inversion}")

	return C
	
def merge_sort(arr):

	n = len(arr)
	no2 = int(n/2)

	#Base case
	if len(arr) == 1:
		return arr

	#acquire halves

	left_half = arr[:no2]
	right_half = arr[no2:]

	# print(f"Left: {left_half}, Right; {right_half} ")
	return merge( merge_sort(left_half), merge_sort(right_half) )


if __name__ == "__main__":
	
	# larr = [6,3,2,1,5,3,2,4,7,12,0,0,12121,1]
	a = [a for a in range(623,0,-1)]
	print(merge_sort(a))
	print(f"Inversion amount: {inversion}")
