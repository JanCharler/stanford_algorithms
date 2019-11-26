from random import randint
from coord_sort import *
import pdb

import matplotlib.pyplot as plt
import matplotlib.patches as patches


P_xvalues = [0,
 1,
 2,
 3,
 5,
 6,
 7,
 8,
 9,
 10,
 12,
 16,
 19,
 24,
 26,
 27,
 30,]

P_yvalues = [ 5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
]

Points = [
	(9, 22),
	(19, 19),
	(0, 25),
	(11, 17), #
	(8, 12),
	(7, 28),
	(14, 28),
	(8, 4),
	(25, 1),
	(26, 24),
	(10, 6),
	(14, 24),
	(4, 19),
	(14, 5),
	(12, 1),
	(7, 20),
	]

# Comment out below for randomized values
graph_value_size = 100
number_of_points = 100

# P_xvalues = {randint(0,graph_value_size) for num in range(0,number_of_points)}
#P_yvalues = [randint(0,graph_value_size) for num in range(0,number_of_points)]
#Points = list(zip(P_xvalues, P_yvalues))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
center_point_xs = []

def ClosestSplitPair(Px, Py, closest_non_split_pair):
	n = len(Px)
	no2 = int(len(Px)/2)
	x_hat = Px[no2][0]

	small_delta = calculate_distance(closest_non_split_pair[0],closest_non_split_pair[1])
	lowest_val = float("inf")
	closesPair = [(0,0),(0,float("inf"))]
	
	# List comprehension of all values inside the range that we want. Big-oh n
	Sy = [val for val in Py if abs(val[0]- x_hat) < small_delta]
	print(f"Sy: {Sy}")
	Sy_n = len(Sy)

	# Brute-force calculate the next points 7 in the y sorted coord list
	for i in range(Sy_n-1):

		for j in range(i+1, min(i+8, Sy_n)):

			print(f"Comparing {Sy[i]} with  {Sy[j]}.")
			dist = calculate_distance(Sy[i], Sy[j])		
			if dist < lowest_val:
				lowest_val = dist
				closesPair =  [Sy[i], Sy[j]] 

	return closesPair
	# plt.show()

def calculate_distance(coor1, coor2):
	'''
	Pass in a tuple of coords
	'''
	# print(f"Coor1: {coor1} and Coor2: {coor2}")
	x1 = coor1[0]
	y1 = coor1[1]

	x2 = coor2[0]
	y2 = coor2[1]

	dist = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) ** 0.5 
	return dist

def find_smallest(left, right):
	'''
	Returns a single tuple
	'''
	#print(f"left: {left} and right: {right}")
	leftmin =  calculate_distance(left[0], left[1])
	rightmin = calculate_distance(right[0], right[1])

	#print(f"Left: {leftmin} and Right: {rightmin} ")
	if leftmin<=rightmin:
		print(f"Winner is {left}, with distance: {leftmin}")
		return left
	else:
		print(f"Winner is {right}, with distance: {rightmin}")
		return right


def closest_pair(Px, Py):
	'''
	Takes in 2 args, Points in ascending order from their X coords and Points in ascending order from their Y coords.
	'''

	# Get number of coords, n
	n = max(len(Px), len(Py))
	n_over_2 = int(n/2)

	# Divide from X coordinate

	x_hat = Px[n_over_2]
	center_point_xs.append(x_hat)

	left_side_x_ordered = Px[:n_over_2]
	left_side_y_ordered = Py[:n_over_2]

	right_side_x_ordered = Px[n_over_2:]
	right_side_y_ordered = Py[n_over_2:]

	# Base case:

	if n <= 3:
		#Return closest pair

		lowest_val = float("inf")
		closesPair = (-1,-1)

		# Save time and return the pair if n = 2
		if n==2:
			return Px

		# Brute-force compare distances
		for i in range(n-1):
			for j in range(i+1,n):

				dist = calculate_distance(Px[i], Px[j])

				if dist < lowest_val:
					lowest_val = dist
					closesPair =  [Px[i],Px[j]] #[(x1,y1),(x2,y2)] 

		print(f"Found closest pair: {closesPair}, with dist: {lowest_val}")
		return closesPair

	else:
		# return find_smallest(closest_pair(left_side_x_ordered, left_side_y_ordered), closest_pair(right_side_x_ordered, right_side_y_ordered))
		ld = closest_pair(left_side_x_ordered, left_side_y_ordered)
		rd = closest_pair(right_side_x_ordered, right_side_y_ordered)

		# Calculate for split coordinates

		smallest_right_left =  find_smallest(ld,rd)
		d_split_pair = ClosestSplitPair(Px, Py, smallest_right_left)

		cp = find_smallest(d_split_pair, smallest_right_left)

		# show_graph(Px, Py, cp)

		return cp

def show_graph(Px, Py, cp,):

	

	n = max(len(Px), len(Py))
	no2 = int(n/2)

	for points in Points:
		plt.plot(points[0], points[1], 'r.')
	
	plt.axis([0, graph_value_size, 0, graph_value_size])

	plt.plot(cp[0][0], cp[0][1], 'g.')
	plt.plot(cp[1][0], cp[1][1], 'g.')
	
	smallestdist = calculate_distance(cp[0], cp[1])
	nline = Px[no2][0]

	delta_over_2 = smallestdist / 2
	small_delta = smallestdist
	x_hat = Px[no2][0]

	
	count = 0
	for points in Points:
		# pdb.set_trace()
		if abs(points[0] - x_hat) < small_delta:

			if count%2 == 0:
					fc = "orange"
			else:
					fc = "orange"
			count+=1
			# Draw 8 squares starting at base of this point
			ypos = points[1]

			for i in range(2):
				xpos = x_hat-small_delta
				for j in range(4):
					ax1.add_patch(
						patches.Rectangle(
							(xpos,ypos),
							delta_over_2,
							delta_over_2,
							alpha=0.3,
							facecolor=fc, edgecolor="black", linewidth=1, linestyle="solid"))
					xpos += delta_over_2
				ypos+=delta_over_2

	plt.plot([nline, nline], [0, graph_value_size], color='k', linestyle='-', linewidth=1)

	plt.show()
	plt.close()


def main():
	
	# Step 1 is to arrange the points in X and Y order.

	Px = merge_sort_coords(Points, 'x')
	Py = merge_sort_coords(Points, 'y')

	
	# Step 2 is to start recursion.

	# Divide:
	cp = closest_pair(Px, Py)
	print(f"function returned: {cp}")

	show_graph(Px, Py, cp,)

	# smallestdist = calculate_distance(cp[0], cp[1])
	# ClosestSplitPair(Px,Py,cp)

	# show_graph(Px, Py, graph_value_size, cp)

	# ax1.add_patch(
	# patches.Rectangle(
	# 	(Px[no2][0]-smallestdist,0),
	# 	smallestdist*2,
	# 	100,
	# 	alpha=0.3,
	# 	facecolor="blue")
	# )


	# ypos = 0
	# for i in range(400):
	# 	xpos = x_hat-small_delta
	# 	for j in range(4):
	# 		ax1.add_patch(
	# 			patches.Rectangle(
	# 				(xpos,ypos),
	# 				delta_over_2,
	# 				delta_over_2,
	# 				alpha=0.3,
	# 				facecolor="orange", edgecolor="black", linewidth=1, linestyle="solid"))

	# 		xpos += delta_over_2
	# 	ypos+=delta_over_2

	

	# Deal with split pair


if __name__ == '__main__':
	main()