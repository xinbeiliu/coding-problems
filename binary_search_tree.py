class BinarySearchTree():
	def __init__(self):
		self.root = None

	def insert(self, data):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
		else:
			current_node = self.root
			while True:
				if data < current_node.data:
					if current_node.left is None:
						current_node.left = new_node
						return
					current_node = current_node.left
				else:
					if current_node.right is None:
						current_node.right = new_node
						return
					current_node = current_node.right
		return

	def lookup(self, data):
		if self.root is None:
			return False
		current = self.root
		while current:
			if current.data == data:
				return True
			elif data < current.data:
				current = current.left
			elif data > current.data:
				current = current.right
		return None

	def BFS(self):
		# [10,5,19,1,20]
		current = self.root
		result = []
		queue = []
		queue.append(current)
		while len(queue) > 0:
			current = queue.pop(0)
			result.append(current.data)
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)
		return result

	def DFS_preorder(self):
		return self.preorder_traversal(self.root, [])

	def DFS_inorder(self):
		return self.inorder_traversal(self.root, [])

	def DFS_postorder(self):
		return self.postorder_traversal(self.root, [])

	def preorder_traversal(self, node, result):
		result.append(node.data)
		if node.left:
			self.preorder_traversal(node.left, result)
		if node.right:
			self.preorder_traversal(node.right, result)
		return result

	def inorder_traversal(self, node, result):
		if node.left:
			self.inorder_traversal(node.left, result)
		result.append(node.data)
		if node.right:
			self.ineorder_traversal(node.right, result)
		return result

	def postorder_traversal(self, node, result):
		if node.left:
			self.postorder_traversal(node.left, result)
		if node.right:
			self.posteorder_traversal(node.right, result)
		result.append(node.data)
		return result

my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(20)
my_tree.insert(170)
my_tree.insert(15)
my_tree.insert(1)
print(my_tree.lookup(170))
print(my_tree.BFS())
print(my_tree.DFS_preorder())
print(my_tree.DFS_inorder())
print(my_tree.DFS_postorder())

# //     9
# //  4     20
# //1  6  15  170