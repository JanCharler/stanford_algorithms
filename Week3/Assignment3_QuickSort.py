import pdb
import re

total_comparisons = 0

def partition(arr, start, stop, pivot_index):
    
    # Put pivot at start
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]

    # Boolean value to prevent us from doing unnecessary work.
    large_val_seen = False
    
    i = start + 1
    n = len(arr)
    
    for j in range(start+1, stop+1):
        if arr[j] > arr[start]:
            # Not interesting case
            large_val_seen = True
            pass
        
        else:
            # Interesting case- the leftmost large value with this value
            if (large_val_seen):
                arr[j], arr[i] = arr[i], arr[j]
            i+=1

    # Swapping the pivot with the (i-1)th element to put pivot in correct place.
    arr[i-1], arr[start] = arr[start], arr[i-1]
    
    return arr, i-1
    

def choose_pivot(arr, start, stop, task):
    
    if task == 1:
        return start
    
    if task == 2:
        return stop
    
    if task == 3:
        
        #Find median of three
        
        arraylength = (stop-start) + 1
        midindex = None
        
        if arraylength == 2:
            return start
        elif arraylength == 1:
            return start
        
        if arraylength%2 == 0:
            midindex = start + int((arraylength / 2) - 1)
        else: # odd
            midindex = start + int(arraylength // 2)

        if arr[start] < arr[midindex] < arr[stop] or arr[start] > arr[midindex] > arr[stop]:
            return midindex
        elif  arr[start] < arr[stop] < arr[midindex] or arr[start] > arr[stop] > arr[midindex]:
            return stop
        elif arr[stop] < arr[start] < arr[midindex] or arr[stop] > arr[start] > arr[midindex]:
            return start
        else:
            print("Shouldn't come here")
            print(f"ARRAY: {arr}")
            print(f"start {arr[start]} mid {arr[midindex]} stop {arr[stop]} ")
            print(f"Just return any one of the three indices here to stop this error.")
            return
            

def quick_sort(arr, start=-1, stop=-1):
    '''
    Sorts an array of any size in nlogn time.
    '''
    
    global total_comparisons
    
    if start == -1 or stop == -1:
        start = 0
        stop = len(arr)-1 # this is the index of the last item

    n = len(arr)
    comp = (stop-start)
    if comp<0: comp = 0
    total_comparisons += comp
    
    # Base case
    if stop-start < 1:
        #print("base")
        #print(arr)
        return arr
    
    # General case
    
    # Choose pivot
    pivot_index = choose_pivot(arr, start, stop, 3)
    arr, p = partition(arr, start, stop, pivot_index)
    
    #left side
    start_left = start
    stop_left = p-1
    if stop_left < start_left: stop_left = start_left
        
    quick_sort(arr, start_left, stop_left)
   
    #right side
    stop_right = stop
    start_right = p+1
    if start_right >= stop_right: start_right = stop_right

    quick_sort(arr, start_right, stop_right)

def check_if_sorted(arr):
    
    for i in range(len(arr)):
        
        j = i+1
        if j >= len(arr):
            return True
        else:
            if arr[i] < arr[j]:
                pass
            else:
                print("Failed")
                return False
                
def main():

	global total_comparisons
	total_comparisons = 0
	

	fileaddr = 'C:\\Users\\Can\\OneDrive\\OneDrive_Documents\\Web\\DataStructuresAndAlgorithms\\TestScripts\\ProgAssignment3TextFile.txt'

	with open(fileaddr, 'r') as f:
	    file = f.read()

	# Store details of file
	reg = r'(\d+)'
	values = re.findall(reg, file)
	# Convert to int
	values = [int(v) for v in values]

	quick_sort(values)
	test = check_if_sorted(values)
	print(total_comparisons)

if __name__ == '__main__':
	main()