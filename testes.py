import random
from arvore import ArvoreBinariaBusca

random.seed(77)

values = random.sample(range(1,1000), 42)

bst = ArvoreBinariaBusca()
for v in values:
	bst.insert(v)

bst.inorder_traversal()

items = [1, 3, 981, 510, 1000]
for item in items:
	r = bst.search(item)
	if r is None:
		print(item, "não encontrado")
	else:
		print(r.root.data, "encontrado")