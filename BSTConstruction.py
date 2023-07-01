# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

"""
﻿
BST Construction✩
Write a BST class for a Binary Search Tree. The class should support:
• Inserting values with the insert method.
Removing values with the remove method; this method should only remove the
first instance of a given value.
Searching for values with the contains method.
Note that you can't remove values from a single-node tree. 
In other words, calling the remove method on a single-node
tree should simply not do anything.
Each BST node has an integer value, a left child node, 
and a right child node. A node is said to be a valid BST node
if and only if it satisfies the BST property: its value is
strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        curNode = self
        newNode = BST(value)
        while True:
                
            if value < curNode.value:
                if curNode.left is None:
                    curNode.left = newNode
                    break
                else:
                    curNode = curNode.left

            else:
                if curNode.right is None:
                    curNode.right = newNode
                    break
                else:
                    curNode = curNode.right
        return self

    def contains(self, value):
        # Write your code here.
        curNode = self
        while curNode is not None:
            #if curNode.value is None:
            #    return False
            if value < curNode.value:
                curNode = curNode.left
            elif value > curNode.value:
                curNode = curNode.right
            else:
                return True
            
        return False
        

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
         
        if self.left is None and self.right is None:
            return self
        
        self.remove2(value, parentNode= None)



    def remove2(self, value , parentNode):

        curNode = self
        while curNode is not None:
            if value < curNode.value:
                parentNode = curNode
                curNode = curNode.left
            elif value > curNode.value:
                parentNode = curNode
                curNode = curNode.right
            else:
                if curNode.left is not None and curNode.right is not None:
                    curNode.value = curNode.right.getMinValue()
                    curNode.right.remove2(curNode.value, curNode)


                elif parentNode is None:
                    if curNode.left is not None:
                        self.value = curNode.left.value
                        self.right =curNode.left.right
                        self.left = curNode.left.left
                    elif curNode.right is not None:
                        self.value = curNode.right.value
                        self.left = curNode.right.left
                        self.right = curNode.right.right
                    else:
                        self.value = None
                        self.left = None
                        self.right = None
                
                elif parentNode.left == curNode:
                    parentNode.left =  curNode.left if curNode.left is not None else curNode.right
                elif parentNode.right == curNode:
                    parentNode.right = curNode.left if curNode.left is not None else curNode.right

                break
  
        return self


    def getMinValue(self):
        
        curNode = self
        while curNode.left is not None:
            curNode = curNode.left
        return curNode.value

            




