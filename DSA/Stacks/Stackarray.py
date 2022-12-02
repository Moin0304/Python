class node :
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
        else:
            new.next=self.head
            self.head=new
        self.size+=1

    

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        self.head=self.head.next
        self.size-=1

    def top(self):
        if self.isempty():
            print("its empty")
            return
        return self.head.data


    def display(self):
        p=self.head
        while p!=None:
            print(p.data,end="-->")
            p=p.next
        print()
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
print(s.top())
s.display()