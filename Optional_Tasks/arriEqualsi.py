import pdb

def checkforai(arr, position, minpos, maxpos):
    '''
    Pass in an array of ascending, distinct integers (negative or positive) and
    returns if there exists a case where arr[i] = i 
    '''
    n = len(arr)
    midpoint = arr[int(position)]
    
    print(minpos, position, maxpos)
    # Base case
    if maxpos-minpos <= 1:
        if midpoint != position:
            return False
    
    # General case

    if midpoint < position:
        minpos = position
        position = (maxpos+position)//2   
        return checkforai(arr, position, minpos, maxpos)
        
    if midpoint > position:
        maxpos = position
        position = (position-minpos)//2
        return checkforai(arr, position, minpos, maxpos)
        
    if midpoint == position:
        return True

def main(testarr = [4,5,8,10,11,14,15,16,18,20]):

    testarr = [4,5,8,10,11,14,15,16,18,20]
    n = len(testarr)

    checkforai(testarr, n//2, 0, n)

if __name__ == '__main__':
    main()