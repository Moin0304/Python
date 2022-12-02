class node:
    def __init__(self,data,next,pre):
        self.data=data
        self.next=None
        self.pre=None
class doubly:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size

    def isempty(self):
        return self.size==0

    def addfirst(self,e):
        new=node(e,None,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head.pre=new
            self.head=new
        self.size+=1

    def addlast(self,e):
        new=node(e,None,None)
        if self.isempty():
            new.next=new
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            new.pre=self.tail
            self.tail=new
        self.size+=1

    def addany(self,e,pos):
        new=node(e,None,None)
        temp=self.head
        i=0
        while i<pos-1:
            temp=temp.next
            i+=1
        new.next=temp.next
        temp.next.pre=new
        temp.next=new
        new.pre=temp
        self.size+=1

    def removefirst(self):
        if self.isempty():
            print("list is empty")
            return
        self.head=self.head.next
        self.head.pre=None
        self.size-=1

    def removelast(self):
        if self.isempty():
            print("list is empty")
            return
        self.tail=self.tail.pre
        self.tail.next=None
        self.size-=1

    def removeany(self,pos):
     def removeany(self,pos):
        if self.isempty():
            print("doubly is empty")
            return
        p=self.head
        i=0
        while i<pos-1:
            p=p.next
            i+=1
        e=p.next.data
        p.next=p.next.next
        p.next.pre=p
        self.size-=1
        return e

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
d=doubly()
d.addfirst(10)
d.addfirst(20)
d.addfirst(30)
d.display()
print()
d.addlast(40)
d.display()
print()
d.addany(50,2)
d.display()
print()
d.removefirst()
d.display()
print()
d.removelast()
d.display()
print()
d.removeany(1)
d.display()