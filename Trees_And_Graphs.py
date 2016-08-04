# Cracking the coding interview - C4 - Trees and Graphs
# Stuart Bradley
# 04-08-2016

# Could have been the flu,
# pretty sure it was the code that
# nearly killed me.

from collections import deque
from itertools import permutations
from random import choice

class Tree_Node:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None

	def traverse_inorder(self, string=""):
		if self.left:
			string += self.left.traverse_inorder()
		string += str(self.name)
		if self.right:
			string += self.right.traverse_inorder()
		return string

# Find route (DFS).
def exercise_1_DFS(graph, start, stop):
	stack = []
	stack.append(start)
	while stack:
		node = stack.pop()
		children = graph[node]
		if stop in children:
			return True
		else:
			stack.extend(children)
	return False

# Find route (BFS).
def exercise_1_BFS(graph, start, stop):
	queue = deque()
	queue.append(start)
	while queue:
		node = queue.popleft()
		children = graph[node]
		if stop in children:
			return True
		else:
			queue.extend(children)
	return False

# Create binary search tree from ordered list.
def exercise_2(items):
	return exercise_2_recursive(items, 0, len(items)-1)

	
def exercise_2_recursive(items, start, end):
	if end < start:
		return None
	mid = (start+end) // 2
	n = Tree_Node(items[mid])
	n.left = exercise_2_recursive(items, start, mid - 1)
	n.right = exercise_2_recursive(items, mid + 1, end)
	return n


# Create depth lists.
def exercise_3(tree):
	depths = []
	# Find root.
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))
	parents = [root]
	while parents:
		children = []
		for parent in parents:
			children.extend(tree[parent])
		depths.append(parents)
		parents = children
	return depths

# Check if tree is balanced.
def exercise_4(tree):
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))
	parents = [root]
	reached_leaf = False
	balance_counter = 2
	while parents:
		children = []
		for parent in parents:
			if len(tree[parent]) < 1:
				reached_leaf = True
			else:
				children.extend(tree[parent])
		if reached_leaf and children:
			balance_counter -= 1
			if balance_counter == 0:
				return False
		parents = children
	return True

# Check if a tree is a binary search tree.
def exercise_5(tree):
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))	
	return exercise_5_recursive_left(tree, root) and exercise_5_recursive_right(tree, root)
	
def exercise_5_recursive_left(tree, parent):
	if len(tree[parent]) > 0:
		child = tree[parent][0]
		if child > parent:
			return False
		else:
			return exercise_5_recursive_left(tree, child) and exercise_5_recursive_right(tree, child)
	else:
		return True
	
def exercise_5_recursive_right(tree, parent):
	if len(tree[parent]) > 1:
		child = tree[parent][1]
		if child <= parent:
			return False
		else:
			return exercise_5_recursive_left(tree, child) and exercise_5_recursive_right(tree, child)
	else:
		return True

# Find successor (parent) of a node in a BST, assumes node is reachable.
def exercise_6(tree, node):
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))
	parent = root
	while True:
		if node <= parent:
			child = tree[parent][0]
		else:
			child = tree[parent][1]
		if child == node:
			return parent
		parent = child

# Find a build path for projects given projects and dependancies
def exercise_7(nodes, paths):
	dependancies = {}
	for n in nodes:
		dependancies[n] = []
	for path in paths:
		dependancies[path[1]].append(path[0])

	build_order = []

	for i in range(len(dependancies)):
		for key in dependancies:
			if not dependancies[key] and (key not in build_order):
				build_order.append(key)
				for key2 in dependancies:
					if key in dependancies[key2]:
						dependancies[key2].remove(key)
	return build_order

# Find common ancestor of two nodes.
def exercise_8(tree, node1, node2):
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))
	reverse_tree = {}
	for node in tree:
		for val in tree[node]:
			if val not in reverse_tree:
				reverse_tree[val] = node

	while node1 != root or node2 != root:
		node1 = reverse_tree[node1]
		node2 = reverse_tree[node2]
		if node1 == node2:
			return node1
	if node1 == node2:
		return root
	else:
		return None

# Determine BST Sequences.
def exercise_9(tree):
	root = min(set(tree.keys()) - set({x for v in tree.values() for x in v}))
	rest = list(tree)
	rest.remove(root)

	possible_arrays = []
	for p in permutations(rest, len(rest)):
		possible_arrays.append([root]+list(p))
	return possible_arrays

# Check if tree2 is a subtree of tree1
def exercise_10(tree1, tree2):
	root1 = min(set(tree1.keys()) - set({x for v in tree1.values() for x in v}))
	root2 = min(set(tree2.keys()) - set({x for v in tree2.values() for x in v}))
	stack = []
	stack.append(root1)
	while stack:
		node = stack.pop()
		if node == root2:
			if exercise_10_subtree(tree1, node, tree2, root2):
				return True
		children = tree1[node]
		stack.extend(children)
	return False

def exercise_10_subtree(tree1, root1, tree2, root2):
	stack1 = []
	stack2 = []
	stack1.append(root1)
	stack2.append(root2)
	while stack1 or stack2:
		node1 = stack1.pop()
		node2 = stack2.pop()
		if node1 != node2:
			return False
		else:
			children1 = tree1[node1]
			children2 = tree2[node2]
			stack1.extend(children1)
			stack2.extend(children2)
	if len(stack1) == len(stack2):
		return True
	else:
		return False

# Return random node. O(n) time.
def exercise_11(tree):
	return choice(tree)

# Count paths to sum.
def exercise_12(tree, amount):
	# Modified find route to deal with change to tree data structure 
	# (so it can hold partial sums).
	incoming_edges = []
	for v in tree.values():
		incoming_edges.extend(v[0])
	root = min(set(tree.keys()) - set(incoming_edges))
	paths = 0
	stack = []
	stack.append(root)
	tree[root][1] = root
	if tree[root][1] == amount:
		paths += 1 
	while stack:
		node = stack.pop()
		children = tree[node][0]
		for child in children:
			res = child + tree[node][1]
			tree[child][1] = res
			if res == amount:
				paths += 1
		stack.extend(children)
	return paths