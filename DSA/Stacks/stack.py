class node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
class stack:
     
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    def push(self,e):
        new=node(e,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
        self.size+=1

    def pop(self):
        self.head=self.head.next
        self.size-=1

    def push1(self,e):
        new=node(e,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new
        self.size+=1
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print()
s.pop()
s.display()
print()
s.push1(50)
s.display()