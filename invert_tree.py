# Python program to demonstrate
# insert operation in binary search tree
from collections import deque
import copy


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def search(root, val):
    if root is None or root.val == val:
        return root  # found or None

    if root.val < val:
        return search(root.right, val)

    return search(root.left, val)


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def levelorder(root):
    if root is None:
        print("N ", end="")
        return

    queue = deque([root])

    while queue:
        curr = queue.popleft()

        if curr is None:
            print("N ", end="")
            continue

        print(curr.val, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# inorder(r)


def mirror(root):
    if root is None:
        return

    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


levelorder(r)
mirror(r)
print()
levelorder(r)
