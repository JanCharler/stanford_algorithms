import pdb
from random import randint


comparisons = 0


def get_highest_and_candidates(leftarr, rightarr):
    '''
    Takes in 2 arrarys with their highest value at index 0
    Returns the max of those two arrays, and candidates for the second max
    '''
    global comparisons
    trail = []
    if leftarr[0] > rightarr[0]:
        comparisons+=1 
        trail = leftarr
        trail.append(rightarr[0])
    
    else:
        comparisons+=1 
        trail = rightarr
        trail.append(leftarr[0])
 
    return trail[0], trail


def get_second_max(arr):
    '''
    Takes in an unsorted array and returns the max of the array, along with
    a narrowed down list of all possible second highest
    '''
    global comparisons
    n = len(arr)
    
    # Base case
    if n == 2:
        if arr[0] > arr[1]:
            comparisons +=1
            return [None], [arr[0], arr[1]]
        else:
            comparisons +=1
            return [None], [arr[1], arr[0]]
    elif n ==1:
        return [None], arr

    # recursive case

    ml, left = get_second_max(arr[:n//2])
    mr, right = get_second_max(arr[n//2:])

    return get_highest_and_candidates(left, right)

def main(testarr =  [2,6,4,10,5,7,8,5,6,21,2,1,4,3,6,2,22,0,3,10,5,7,8,5,6,21,2,1,4,3,6]):
    '''
    Pass in array to return max, second max, and number of comparisons done.
    '''

    global comparisons 
    comparisons = 0

    first_max, candidates = get_second_max(testarr)
    print(first_max,)

    second_max, _ = get_second_max(candidates[1:])
    print(second_max)

    print(comparisons)

if __name__ == '__main__':
    main()