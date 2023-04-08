#!/usr/bin/python3
import math

class Node:
    def __init__(self):
        self.weight = 0
        self.maxWeightIncluded = -math.inf
        self.maxWeightExcluded = -math.inf
        self.left = self.right = None

# A utility function to create a node
def newNode(weight) :
    node = Node()
    node.weight = weight
    node.left = node.right = None
    return node

## Helper functions for printing the tree - start
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1

def getcol(h):
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1
 
 
def printTree(M, root: Node, col, row, height):
    if root is None:
        return
    M[row][col] = (root.weight, root.maxWeightIncluded, root.maxWeightExcluded)
    printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
    printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
def TreePrinter(root):
    h = height(root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, root, col//2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print("   ", end="   ")
            else:
                print(j, end="   ")
        print("")

## Helper functions for printing the tree - end

def maxWeightNotIncluding(node):
    if node == None:
        return 0
    
    if node.maxWeightExcluded != -math.inf: # make use of the memo table
        return node.maxWeightExcluded
    
    if node.left == None and node.right == None: # leaf node base case
        node.maxWeightExcluded = 0
        return node.maxWeightExcluded
    
    node.maxWeightExcluded = max(maxWeightIncluding(node.left), maxWeightNotIncluding(node.left)) + \
                                 max(maxWeightIncluding(node.right), maxWeightNotIncluding(node.right)) # recurse
    return node.maxWeightExcluded

def maxWeightIncluding(node):
    if node == None:
        return 0
    
    if node.maxWeightIncluded != -math.inf: # make use of the memo table
        return node.maxWeightIncluded
    
    if node.left == None and node.right == None: # leaf node base case
        node.maxWeightIncluded = node.weight
        return node.maxWeightIncluded
    
    node.maxWeightIncluded = node.weight + maxWeightNotIncluding(node.left) + maxWeightNotIncluding(node.right) # recurse
    return node.maxWeightIncluded

# def get_node_set(root: Node, ans: list, is_parent_selected: bool):
#     if root: # perform pre-order tree traversal
#         if root.maxWeightIncluded > root.maxWeightExcluded and not is_parent_selected:
#             ans.append(root.weight)
#             is_parent_selected = True
#         else:
#             is_parent_selected = False
#         get_node_set(root.left, ans, is_parent_selected)
#         get_node_set(root.right, ans, is_parent_selected)
#         return ans

def get_node_set(root: Node, ans: list):
    if root: # perform pre-order tree traversal
        if root.maxWeightIncluded > root.maxWeightExcluded: # include node and go to grandchildren
            ans.append(root.weight)
            if root.left != None and root.right != None: # skip traversal if leaf node
                get_node_set(root.left.left, ans)
                get_node_set(root.left.right, ans)
                get_node_set(root.right.left, ans)
                get_node_set(root.right.right, ans)
        else: # go to children 
            get_node_set(root.left, ans)
            get_node_set(root.right, ans)
    return ans
    

def create_tree():
    root = newNode(1.9)
    root.left = newNode(2)
    root.left.left = newNode(1)
    root.right = newNode(0.8)
    root.right.left = newNode(2.3)
    root.right.left.left = newNode(1.7)
    root.right.left.right = newNode(0.5)
    root.right.right = newNode(0.1)
    root.right.right.left = newNode(4)
    return root

def create_tree_2():
    root = newNode(5)
    root.left = newNode(2)
    root.left.left = newNode(1)
    root.left.right = newNode(0)
    root.right = newNode(4)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    return root

def create_tree_3():
    root = newNode(1.9)
    root.left = newNode(2)
    root.left.left = newNode(1)
    root.right = newNode(8)
    root.right.left = newNode(2.3)
    root.right.left.left = newNode(1.7)
    root.right.left.right = newNode(0.5)
    root.right.right = newNode(0.1)
    root.right.right.left = newNode(4)
    return root

def create_tree_4():
    root = newNode(-5)
    root.left = newNode(-4)
    root.right = newNode(-2)
    return root

def main():
    root = create_tree()
    maxWeight = max(maxWeightIncluding(root), maxWeightNotIncluding(root))
    print(maxWeight)
    ans = get_node_set(root, [])
    print(ans)
    TreePrinter(root)

if __name__ == "__main__":
    main()