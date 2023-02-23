"""Binary Search Tree (BST)"""
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def insert(self, data):
        pNew = BSTNode(data)
        if self.root is None:
            self.root = pNew
            return
        pos = self.root
        while pos is not None:
            if data < pos.data:
                if pos.left is None:
                    pos.left = pNew
                    return
                else:
                    pos = pos.left
            else:
                if pos.right is None:
                    pos.right = pNew
                    return
                else:
                    pos = pos.right
    def preorder(self, root):
        if root != None:
            print("-> " + str(root.data), end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if root != None:
            self.preorder(root.left)
            print("-> " + str(root.data), end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("-> " + str(root.data), end=" ")
    def traverse(self):
        print("Preorder : ", end="")
        self.preorder(self.root)
        print("\nInorder : ", end="")
        self.inorder(self.root)
        print("\nPostorder : ", end="")
        self.postorder(self.root)
        print()
    def findMin(self, root=None):
        if root is None:
            pos = self.root
            while pos.left is not None:
                pos = pos.left
            return pos.data
        else:
            start = root
            while start.left is not None:
                prev = start
                start = start.left
            try:
                return prev
            except:
                return start
    def findMax(self, root=None):
        if root is None:
            pos = self.root
            while pos.right is not None:
                pos = pos.right
            return pos.data
        else:
            start = root
            log = start.data
            while start.right != None:
                prev = start
                start = start.right
            try:
                return prev
            except:
                return start
    def delete(self, dlt_key):
        if self.root is None:
            return print("Cannot Delete Node Kaa")
        elif self.root.data == dlt_key:
            # ! case node that wants to delete is root
            # case node that wants to delete has not subtree
            if self.root.left is None and self.root.right is None:
                self.root = None
            # case node that wants to delete has one sebtree
            else:
                try:
                    replace = self.findMax(self.root.left)
                    self.root.data = replace.right.data
                    replace.right = None
                except:
                    replace = self.findMin(self.root.right)
                    self.root.data = replace.left.data
                    replace.left = None
        else:
            # set prev and start
            prev = self.root
            if dlt_key < prev.data:
                start  = prev.left
            else:
                start = prev.right

            # find the node that wants to delete
            while start.data != dlt_key:
                if dlt_key < start.data:
                    prev, start = start, start.left
                else:
                    prev, start = start, start.right

            # * --- delete node ---
            # case node that wants to delete has not subtree
            if start.left is None and start.right is None:
                if start.data < prev.data:
                    prev.left = None
                else:
                    prev.right = None
            # case node that wants to delete has one sebtree
            elif not (start.left is not None and start.right is not None):
                if start.left is not None:
                    if start.data < prev.data:
                        prev.left = start.left
                    else:
                        prev.right = start.left
                else:
                    if start.data < prev.data:
                        prev.left = start.right
                    else:
                        prev.right = start.right
            # case node that wants to delete has two subtrees
            else:
                replace = self.findMax(start.left)
                start.data = replace.right.data
                replace.right = None

myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.traverse()
myBST.delete(14)
myBST.traverse()
print(myBST.findMin())
print(myBST.findMax())