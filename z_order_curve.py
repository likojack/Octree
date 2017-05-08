import numpy as np
import math
# python implementation for z order curve representation for octtree
# X for the spatial position for a point X: (x,y,z), l is the level of the tree, width is the size of space

class Octtree():
	def __init__(self, size):
		self.locationCode = {}
		self.size = size

#convert a 3D point coordinate to the morton code of octree at level l
def location_code(X,l,tree):
	code = "1" # state the end of locational code
	width = tree.size
	assert (l <= math.log(width, 2)),"the level exceed the size of space"
	assert (X[0] <= width-1 and X[1] <= width-1 and X[2] <= width-1), "the spatial point exceed the size of space"
	for i in range(l):
		# 0 means the point in the left side of this axis, otherwise, on the right side
		partition_x = str(math.floor(X[0]/(width/2))) 
		partition_y = str(math.floor(X[1]/(width/2)))
		partition_z = str(math.floor(X[2]/(width/2)))
		code = code + partition_x + partition_z + partition_y
		width = width / 2 # to the next level of the tree, half space size
		if partition_y == str(1):
			X[1] = X[1] - width
		if partition_z == str(1):
			X[2] = X[2] - width
		if partition_x == str(1):
			X[0] = X[0] - width
	return int(code, base = 10) # convert to binary number

def get_parent(locational_code):
	if(isinstance(locational_code,str)):
		locational_code = int(locational_code,base = 10)
	return locational_code >> 3


tree = Octtree(4)
X = (0,0,0)
print(location_code(X,1,tree))
