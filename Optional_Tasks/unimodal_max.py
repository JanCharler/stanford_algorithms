'''
Optional question 2.
Finds maximum element in a unimodal array in O(logn) time.
'''

steps = 0
def find_unimodal_max(arr):
     
    global steps
    n = len(arr)
    nby2 = n//2
    print(arr)
    
    if n == 0:
        steps+=1
        return False
    if n < 2:
        steps+=1
        return max(arr)
    else:
        if arr[nby2-1] < arr[nby2] < arr[nby2+1]:
            steps+=1
            #Upwards slope
            return find_unimodal_max(arr[n//2:])
        
        if arr[nby2-1] < arr[nby2] < arr[nby2+1]:
            steps+=1
            #Downwards slope
            return find_unimodal_max(arr[:n//2])
    
        if arr[nby2-1] < arr[nby2] > arr[nby2+1]:
            steps+=1
            return arr[nby2]
            
