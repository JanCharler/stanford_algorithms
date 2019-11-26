# Practicing recursive calls by testing on factorials and fib numbers
def factorial(n):

	if (n == 0):
		return 1

	return n * factorial(n-1)

def fib(n):

	if n==2:
		return 1
	if n==1:
		return 1

	if n>2:
		 answer = fib(n-1) + fib(n-2)
		 print("answer is: " + str(answer))
		 return answer

	else:
		return 1