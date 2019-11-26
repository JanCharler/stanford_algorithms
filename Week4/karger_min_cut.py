import re
import random
import pdb
import copy
import timeit

def create_adj_dict(al):
    '''
    Creates adjacency dict from adjacency list where the
    adjacency list is comprised of a list of lists each inner list
    containing the vertex number in the first entry and the rest showing
    which other vertices that vertex shares an edge with.
    '''
    
    adjdict = {}
    newlist = al.copy() # Copy passed in list
    
    for row in newlist:
        if len(row) > 0:
            temprow = row.copy()
            vertex = temprow.pop(0) # Copy row so values are not affected in org list
            adjdict[vertex] = temprow
    return adjdict

def convert_file_to_a_list_entry():
    '''
    Converts .txt file from Stanford to a list entry in 
    format [[vertex, neighbour1, neighbour2], [vertex2, neighbour1]]...
    '''
    # Reading test file
    addr = "C:\\Users\\Can\\OneDrive\\OneDrive_Documents\\Web\\DataStructuresAndAlgorithms\\TestScripts\\kargerMinCutItems.txt"
        
    with open(addr, 'r') as k:
        txtfile = k.read()

    # Split rows
    rows = txtfile.split("\n")

    # Create list of rows found in adj list from the file
    l = []
    for row in rows:
        r = row.split("\t")
        r.remove("")
        l.append(r)

    # Convert entries to ints
    adjlist = []
    for row in l:
        adjlist.append(list(map(lambda entry: int(entry), row)))

    # Convert adjacency list to a dictionary
    return adjlist
    

def merge_vertices(adict, vertex, edge):
    '''
    Combines the vertices and removes self loops
    '''
    
    # Step 1 merge the two dict entries
    firstVertex = vertex
    secondVertex = edge
    adict[firstVertex].extend(adict[secondVertex]) #merge vertices
    
    # Step 2 change neighbours of second vertex to now point to firstVertex
    for i in range(len(adict[secondVertex])):
        second_vertex_neighbour = adict[secondVertex][i]
        
        for i in range(len(adict[second_vertex_neighbour])):
            if adict[second_vertex_neighbour][i] == secondVertex:
                adict[second_vertex_neighbour][i] = firstVertex
    
    # Step 3 remove secondVertex as it is now fully merged to firstVertex
    adict.pop(secondVertex) # remove second vertex entries

    # Step 4 remove self loops
    while firstVertex in adict[firstVertex]:
        adict[firstVertex].remove(firstVertex)
        
    while secondVertex in adict[firstVertex]:
        adict[firstVertex].remove(secondVertex)


# Karger's Random Contraction Algorithm
def r_contraction(adict):
    '''
    Pass in an adjacency list (in dict form) and will
    return 2 merged vertices with the number of cuts.
    Dict syntax: {vertex:[neighbouringVertex1, neighbouringVertex2], vertex2:[neigh...]}
    '''
    
    # While more than 2 vertices:
    while len(adict.keys()) > 2:
        
        # Pick a remaining edge uniformly at random
        random_vertex = random.choice(list(adict)) 
        random_edge = random.choice(adict[random_vertex])  

        # Merge (or "contract") u and v into a single vertex
        merge_vertices(adict, random_vertex, random_edge)

    # Return cut represented by final 2 vertices
    lengths = []
    for v in adict.values():
        lengths.append(len(v))
    return lengths

def run_contraction_algorithm(n = 10):
    counter = 0
    lowest_val = float("inf")
    adjlist = convert_file_to_a_list_entry()
    adjdict = create_adj_dict(adjlist)

    for i in range(n):
        counter+=1

        list_of_merged_vertices = {}
        adjdict_copy = copy.deepcopy(adjdict)
        result = r_contraction(adjdict_copy)

        if result[0] != result[1]:
            print("ERROR, MERGING") # added for debug.
            raise 
        else:
            if result[0] < lowest_val:
                lowest_val = result[0]
        if counter%100 == 0:
            print(counter)
        print(f"Result: {result[0]}")

    print(f"Lowest: {lowest_val}")

run_contraction_algorithm()