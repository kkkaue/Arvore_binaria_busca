class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

class ArvoreBinaria:
	def __init__(self,data=None,node = None):
		if node:
			self.root = node
		elif data:
			node = Node(data)
			self.root = node
		else:
			self.root = None

	def simetric_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			print("(", end = "")
			self.simetric_traversal(node.left)
		print(node, end = "")
		if node.right:
			self.simetric_traversal(node.right)
			print(")", end = "")

	def postorder_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			self.postorder_traversal(node.left)
		if node.right:
			self.postorder_traversal(node.right)
		print(node)

	def heigth(self, node=None):
		if node is None:
			node = self.root
		hleft = 0
		hright = 0
		if node.left:
			hleft = self.heigth(node.left)
		if node.right:
			hright = self.heigth(node.right)
		if hright>hleft:
			return hright + 1
		return hleft + 1

	def inorder_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			self.inorder_traversal(node.left)
		print(node, end = " ")
		if node.right:
			self.inorder_traversal(node.right)

class ArvoreBinariaBusca(ArvoreBinaria):
	def insert(self,value):
		parent = None
		x = self.root
		while(x):
			parent = x
			if value < x.data:
				x = x.left
			else:
				x = x.right
		if parent is None:
			self.root = Node(value)
		elif value < parent.data:
			parent.left = Node(value)
		else:
			parent.right = Node(value)

	def search(self, value):
		return self._search(value, self.root)

	def _search(self, value, node):
		if node is None:
			return node
		if node.data == value:
			return ArvoreBinariaBusca(node)
		if value < node.data:
			return self._search(value, node.left)
		else:
			return self._search(value, node.right)

		# def search(self, value, node=0):
		# 	if node == 0:
		# 		node = self.root
		# 	if node is None or node.data == value:
		# 		return ArvoreBinariaBusca(node)
		# 	if value < node.data:
		# 		return self.search(value, node.left)
		# 	else:
		# 		return self.search(value, node.right)

if __name__ == '__main__':
	# arvore = ArvoreBinaria()
	# n1 = Node('a')
	# n2 = Node('+')
	# n3 = Node('*')
	# n4 = Node('b')
	# n5 = Node('-')
	# n6 = Node('/')
	# n7 = Node('c')
	# n8 = Node('d')
	# n9 = Node('e')

	# n6.left = n7
	# n6.right = n8
	# n5.left = n6
	# n5.right = n9
	# n3.left = n4
	# n3.right = n5
	# n2.left = n1
	# n2.right = n3

	# arvore.root = n2	

	# arvore.simetric_traversal()
	# print("")

	arvore = ArvoreBinaria()
	n1 = Node('I')
	n2 = Node('N')
	n3 = Node('S')
	n4 = Node('C')
	n5 = Node('R')
	n6 = Node('E')
	n7 = Node('V')
	n8 = Node('A')
	n9 = Node('5')
	n0 = Node('3')

	n0.left = n6
	n0.right = n9
	n6.left = n1
	n6.right = n5
	n5.left = n2
	n5.right = n4
	n4.right = n3
	n9.left = n8
	n8.right = n7

	arvore.root = n0

	print("Percurso em pós ordem:")
	arvore.postorder_traversal()
	print("altura: ", arvore.heigth())