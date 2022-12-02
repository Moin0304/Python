class node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size==0

    def enq(self,e):
        new=node(e,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new
        self.size+=1

    def deq(self):
        if self.isempty():
            print("its empty")
            return
        self.head=self.head.next
        self.size-=1


    
    def display(self):
        p=self.head
        while p!=None:
            print(p.data,end="-->")
            p=p.next
        print()
q=queue()
q.enq(1)
q.enq(2)
q.enq(3)
q.display()
q.deq()
q.display()