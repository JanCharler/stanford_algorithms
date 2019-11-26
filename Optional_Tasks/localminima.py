import pdb
from random import randint
import numpy as np


# Draw cross on matrix, find minimum
def find_min_window(mat):
    
    height = mat.shape[0]
    width = mat.shape[1]
    
    half_height = height // 2
    half_width = width // 2
    
    minimum = float("inf")
    minrow = 0
    mincol = 0
    
    # Window top frame
    for i in range(width):
        if mat[0, i] < minimum:
            minimum = mat[0, i]
            minrow = 0
            mincol = i
    
    # Window bottom frame
    for i in range(width):
        if mat[height-1, i] < minimum:
            minimum = mat[height-1, i]
            minrow = height-1
            mincol = i
            
    # Window left vertical frame
    for i in range(height):
        if mat[i, 0] < minimum:
            minimum = mat[i, 0]
            minrow = i
            mincol = 0
            
    # Window right vertical frame
    for i in range(height):
        if mat[i, width-1] < minimum:
            minimum = mat[i, width-1]
            minrow = i
            mincol = width-1
    
    
    # Middle vertical
    for i in range(height): 
        if mat[i, half_width] < minimum:
            minimum = mat[i, half_width]
            minrow = i
            mincol = half_width
    
    # Midle horizontal
    for j in range(width):
        if mat[half_height, j] < minimum:
            minimum = mat[half_height, j]
            minrow = half_height
            mincol = j
            
    #pdb.set_trace()
    return {'val':minimum, 'row':minrow,'col':mincol, 'height':height,'width':width}


# Check neighbours
def check_if_local_minima(mat, row, col):
    '''
    Checks position in matrix and returns True if local minimum.
    Or false if not.
    If true, also returns the point.
    If false, also returns the neighbouring lowest.
    '''

    # Check neighbour above
    x = row-1
    if x<0:
        above = {'val': float("inf"), 'row': x, 'col': col, 'neighbour': 'above'}
    else:
        above = {'val': mat[x, col], 'row': x, 'col': col, 'neighbour': 'above'}
    
    # Check neighbour below
    x = row+1
    if x >= mat.shape[0]:
        below = {'val': float("inf"), 'row': x, 'col': col, 'neighbour': 'below'}  
    else:
        below =  {'val': mat[x, col], 'row': x, 'col': col, 'neighbour': 'below'} 
    
    # Check neighbour right
    y = col+1
    if y >= mat.shape[1]:
        right = {'val': float("inf"), 'row': row, 'col': y, 'neighbour': 'right'} 
    else:
        right = {'val': mat[row, y], 'row': row, 'col': y,'neighbour': 'right'}  
    
    # Check neighbour left
    y = col-1
    if y<0:
        left = {'val':  float("inf"), 'row': row, 'col': y, 'neighbour': 'left'}  
    else:
        left = {'val':  mat[row, y], 'row': row, 'col': y, 'neighbour': 'left'}  
        
    # Comparing neighbours with center point
    myPoint = {'val': mat[row,col], 'row': row, 'col': col}  

    # Is a local minimum, return this.
    if myPoint['val'] < above['val'] and myPoint['val'] < below['val'] and \
            myPoint['val'] < left['val'] and myPoint['val'] < right['val']:
        return myPoint, True
    
    # Not local minimum, returning lowest neighbour anyway
    else:
        min_neighbour = {'val':float("inf")}
        neighbours = [above, below, left, right]
        for neighbour in neighbours:
            if neighbour['val'] < min_neighbour['val']:
                min_neighbour = neighbour
        return min_neighbour, False

def brute_force_local_minima(mat):
    local_minima = []
    a = "result"
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            a, result = check_if_local_minima(mat, i, j)
            if result:
                local_minima.append((a, result))
    return local_minima
    
                
def big_oh_n_local_minima(mat):
    
    rows = mat.shape[0]
    cols = mat.shape[1]
    
    # Base case- Only one element remains
    if mat.shape == (1,1):
        return check_if_local_minima(mat, 0, 0)
    #elif mat.shape == (2,2):
        #return check_if_local_minima(mat, 0, 0) # If the cross isn't minimum, check the top left section
    elif mat.shape == (0,0):
        return False
    
    # Find minimum of cross
    mincross = find_min_window(mat) #find_cross_minimum(mat)
    
   # print(f"Minimum within cross: {mincross}")
    
    # check if local minima
    value_returned, is_minima = check_if_local_minima(mat, mincross['row'], mincross['col'])
    #print(value_returned, is_minima)
    
    # General case
    #print(mat)

    if is_minima:
        #print("Found minima!")
        return value_returned, is_minima
    
    # Not found minima, see where neighbour was
    else:
        
        #print("Dividing mat...")

        # Divide matrix depending on where neighbour is
        newmatr = np.mat(np.zeros(shape=(2,2)))
    
        if value_returned['row'] < rows//2:
            #print("NEIGHBOUR IS TOP LEFT")   
            if value_returned['col'] < cols//2:
                newmatr = mat[:rows//2+1,:cols//2+1]
            
            #print("NEIGHBOUR IS TOP RIGHT") 
            elif value_returned['col'] > cols//2:
                newmatr = mat[:rows//2+1,cols//2:]
            else:
                print("Error shouldn't come here: (#1)")
             
        elif  value_returned['row'] > rows//2:
            #print("NEIGHBOUR IS BOTTOM LEFT")  
            if value_returned['col'] < cols//2:
                newmatr = mat[rows//2:,:cols//2+1]
            
            #print("NEIGHBOUR IS BOTTOM RIGHT")
            elif value_returned['col'] > cols//2:
                
                newmatr = mat[rows//2:,cols//2:]
            else:
                print("Error shouldn't come here: (#2)")
                
        else:
            print("Shouldn't come here (#3)")
        
        #print(f"Divided mat: {newmatr}")        
        return big_oh_n_local_minima(newmatr)

# Create an empty matrix of size n by n
def randomise_mat(n=8):
    
    mat = np.mat(np.zeros(shape=(n,n)))
    count = n*n
    for i in range(n):
        for j in range(n):

            while True:
                random_number =  randint(0,n*n*n)
                if random_number not in mat:
                    mat[i,j] = random_number # 
                    count-=1
                    break
    return mat

# Unit testing

def unittest(n = 100):
    '''
    How many iterations should we test?
    Compares against brute force algorithm.
    '''
    testcount = 0
    correctcount= 0
    wrongcount = 0

    for i in range(n):
        
        newmat = randomise_mat(randint(1,10))
        #print("test started")
        #print(newmat)
        brute_result = brute_force_local_minima(newmat)
        brute_result_values = [value['val'] for value,passfail in brute_result]
        mytest_result, passfail = big_oh_n_local_minima(newmat)
        testcount+=1
        #print(newmat)
        #print(mytest_result['val'])
        #print(brute_result_values)
        if correctcount%2000 == 0:
            print(correctcount)
        if mytest_result['val'] in brute_result_values:
            correctcount +=1
        else:
            wrongcount +=1
            print("WRONG ABOVE HERE")
        #print("test finished")
    print(f"Correct: {correctcount} and Wrong: {wrongcount}")

def main():

    newmat = randomise_mat(randint(1,10))
    print("Test started")
    print(newmat)
    result, passfail = big_oh_n_local_minima(newmat)
    print(f"Found local minima: {passfail}, Result: {result['val']}")

if __name__ == '__main__':
    main()