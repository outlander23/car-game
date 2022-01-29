# Python program to check if rectangles overlap
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Returns true if two rectangles(l1, r1)
# and (l2, r2) overlap
def doOverlap(l1, r1, l2, r2):
	
	# To check if either rectangle is actually a line
	# For example : l1 ={-1,0} r1={1,1} l2={0,-1} r2={0,1}
	
	if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
		# the line cannot have positive overlap
		return False
	
	
	# If one rectangle is on left side of other
	if(l1.x >= r2.x or l2.x >= r1.x):
		return False

	# If one rectangle is above other
	if(r1.y >= l2.y or r2.y >= l1.y):
		return False

	return True

# Driver Code
if __name__ == "__main__":
	l1 = Point(0, 10)
	r1 = Point(10, 0)
	l2 = Point(5, 5)
	r2 = Point(15, 0)

	if(doOverlap(l1, r1, l2, r2)):
		print("Rectangles Overlap")
	else:
		print("Rectangles Don't Overlap")

# This code is contributed by Vivek Kumar Singh
