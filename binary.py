class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


def findMax(root):

	
	if (root == None):
		return float('-inf')

	
	node = root.data
	tree = findMax(root.left)
	branch = findMax(root.right)
	if (tree > node):
		node = tree
	if (branch > node):
		node = branch
	return node


if __name__ == '__main__':
	root = newNode(2)
	root.left = newNode(7)
	root.right = newNode(5)
	root.left.right = newNode(6)
	root.left.right.left = newNode(1)
	root.left.right.right = newNode(11)
	root.right.right = newNode(9)
	root.right.right.left = newNode(4)

	
	print("Maximum element is",
		findMax(root))