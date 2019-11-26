
def karatsuba(num1, num2):
	'''
	Multiplies 2 integers num1 and num2 where they are both the same length
	'''

	# Convert number 1 and 2 to string
	num1 = str(num1)
	num2 = str(num2)
	print(f"Num1: {num1}")
	print(f"Num2: {num2}")

	# Get length of each number
	n1 = len(str(num1))
	n2 = len(str(num2))

	# Need to implement so it works for inputs other than power of 2.
	# If odd indeces long before base case, add 0 to the start
	# if max(n1, n2) == 2 and abs(n1-n2) == 1:
	# 	if n1 < n2:
	# 		num1 = "0" + num1
	# 	elif n2 < n1:
	# 		num2 = "0" + num2

	# Store max length and half length for the calculations
	n = max(n1, n2)
	n_over_2 = int(n/2)

	# Base case, 1 digit at most
	if n == 1:
		ans = int(num1)*int(num2)
		return ans
	
	a = (num1[:n_over_2])
	b = (num1[n_over_2:] )

	c = (num2[:n_over_2] )
	d = (num2[n_over_2:] )

	ac = karatsuba(a,c) 
	bd = karatsuba(b,d)

	ad = karatsuba(a,d)
	bc = karatsuba(b,c)

	# The algorithm
	return (10**n)*ac + ((10**n_over_2) * (ad + bc)) + bd

if __name__ == '__main__':
	
	# Multiplying two digits
	n1 = 1598
	n2 = 4231
	a = karatsuba(n1 , n2)
	with open('answer.txt',mode='w') as myfile:
		print("Writing tofile")
		myfile.write(str(a))
	print(f"Multiplying {n1} by {n2}")
	print(f"Answer is {a}")