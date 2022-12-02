
class node:
    __slots__ = "element","left","right"
    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right
    

class binary_tree:
    def __init__(self):
        self.root = None

    def maketree(self,e,left,right):
        self.root = node(e,left.root,right.root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)
    
    def preorder(self,troot):
        if troot:
            print(troot.element,end=" ")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element,end=' ')

    # def levelorder(self,troot):
    #     Q = queueslinked()
    #     t = self.root
    #     print(t.element,end=" ")
    #     Q.enqueue(t)
    #     while not Q.isempty():
    #         t = Q.dequeue()
    #         if t.left:
    #             print(t.left.element,end=" ")
    #             Q.enqueue(t.left)
    #         if t.right:
    #             print(t.root.element,end=' ')
    #             Q.enqueue(t.right)

    def count(self,troot):
        if troot:
            x = self.count(troot.left)
            y = self.count(troot.right)
            return x+y+1
        return 0

    def height(self,troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

x=binary_tree()
y=binary_tree()
z=binary_tree()
a=binary_tree()
# r=binary_tree()
# s=binary_tree()
# t=binary_tree()
x.maketree(40,a,a)
y.maketree(50,a,a)
z.maketree(30,x,y)
# r.maketree(50,a,y)
# s.maketree(30,r,a)
# t.maketree(10,z,s)
print("inorder traversel")
z.inorder(z.root)
print()
print("preorder traversel")
z.preorder(z.root)
print()
print("postorder traversel")
z.postorder(z.root)
print()
print("number of nodes")
print(z.count(z.root))
print("height")
print(z.height(z.root)-1)