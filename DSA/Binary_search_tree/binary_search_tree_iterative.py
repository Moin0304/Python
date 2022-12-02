class node:
    __slots__ = "element","left","right"
    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

class binary_search_tree_iterative:
    def __init__(self):
        self.root = None
    
    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e == troot.element:
                return
            elif e < troot.element:
                troot = troot.left
            elif e > troot.element:
                troot = troot.right
        n = node(e)
        if self.root:
            if e < temp.element:
                temp.left = n
            else:
                temp.right = n
        else:
            self.root = n

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end='')
            self.inorder(troot.right)

b = binary_search_tree_iterative
b.insert(b.root,10)
b.insert(b.root,20)
b.insert(b.root,30)
b.inorder(b.root)