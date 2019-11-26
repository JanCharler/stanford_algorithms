'''
Optional question: Merge k arrays of size n.
'''


def merge(arr1, arr2):
	'''
	Pass in 2 sorted arrays
	'''
	resultarr = [None]* (len(arr1) + len(arr2))

	i = 0
	j = 0
	k = 0
	opnum = 0;

	for k in range(len(resultarr)):

		if i>= len(arr1):
			# arr1 is exhausted, fill rest of result arr with arr2
			# print("arr 1 exhausted")
			while k < len(resultarr):

				resultarr[k] = arr2[j]
				k+=1
				j+=1
			#print(resultarr)
			return resultarr
		elif j>=len(arr2):
			# print("arr 2 exhausted")

			while k < len(resultarr):
				# print("k is" + str(k))
				resultarr[k] = arr1[i]
				k+=1
				i+=1
			#print(resultarr)
			return resultarr

		# print(i)

		if arr1[i] < arr2[j]:
			resultarr[k] = arr1[i]
			i+=1
		else:
			resultarr[k] = arr2[j]
			j+=1

def k_merge(*args):

	arrlist = args
	merged = arrlist[0]

	for i in range(len(arrlist)-1):
		print("len of merged is; " + str(len(merged)))
		merged = merge(merged, arrlist[i+1])

	print(merged)

if __name__ == "__main__":
	
	k_merge([5,6], [4,10], [1,9], [2,4],[1,10],[0,100],[3,4])
