import re
import pdb

total_inversions = 0

def sort_ordered(leftarr, rightarr):
    global total_inversions
    
    totallen = len(leftarr) + len(rightarr)
    j = 0
    k = 0
    resultarr = [None] * totallen
    
    for i in range(totallen):
        # End cases
        if k >= (len(rightarr)):
            resultarr[i] = leftarr[j]
            j+=1
            continue
            
        elif j >= (len(leftarr)):            
            resultarr[i] = rightarr[k] 
            k+=1
            continue
        
        # Comparison
        if leftarr[j] <= rightarr[k]:
            resultarr[i] = leftarr[j]
            j+=1
            
        elif rightarr[k] < leftarr[j]:
            resultarr[i] = rightarr[k] 
            
            # Interesting case, add inversion number to total inversions. 
            # Inversion number is however many values still remaining in the left array.
            total_inversions += len(leftarr)- j
            k+=1  
            
    return resultarr
    
def sort_and_count_inversions(arr):

    n = len(arr)
    nover2 = int(n/2)
    leftarr = arr[:nover2]
    rightarr = arr[nover2:]

    # Base case
    if n < 2:
        return arr

    # Divide
    l = sort_and_count_inversions(leftarr)
    r = sort_and_count_inversions(rightarr)
    return sort_ordered(l, r)

def main(text_file):

	#Saving the array to a list
	myarr = []
	pattern = r"\d+"

	with open(addr, 'r') as f:
	    for v in f:
	        nums = (re.findall(pattern, v))[0]
	        myarr.append(int(nums))

	testarr = [1,4,3,2,1,5,4,3]
	sortAndCount(testarr)

if __name__ == '__main__':

	addr = "C:\\Users\\Can\\OneDrive\\OneDrive_Documents\\Web\\DataStructuresAndAlgorithms\\TestScripts\\100karray.txt"
	listofnumbers = []
	#Regex pattern to grab the numbers from the text file
	pattern = r"\d+"

	with open(addr, 'r') as f:
	    for v in f:
	        nums = (re.findall(pattern, v))[0]
	        listofnumbers.append(int(nums))

	sort_and_count_inversions(listofnumbers)
	print("Total inversions: " + str(total_inversions))