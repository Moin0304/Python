class node:
    def __init__(self,data,next):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    def addlast(self,n):
        new = node(n,None)
        if self.isempty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size+=1



    def removenthnodefromlast(self,n):
        p = self.head
        i=0
        while i<len(self)-n-1:
            p = p.next
            i+=1
        p.next = p.next.next
        self.size-=1


    def display(self):
        p = self.head
        while p:
            print(p.data,end="->")
            p = p.next
        
        
l=linked()
l.addlast(10)
l.addlast(20)
l.addlast(30)
l.addlast(40)
l.addlast(50)
l.removenthnodefromlast(2)
l.display()