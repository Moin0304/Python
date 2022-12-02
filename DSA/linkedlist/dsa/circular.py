class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class cir:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    def addfirst(self,e):
        new=node(e,None)
        if self.isempty():
            new.next=new
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            new.next=self.head
            self.head=new
        self.size+=1

    def addlast(self,e):
        new=node(e,None)
        if self.isempty():
            new.next=new
            self.head=new
            self.tail=new
        else:
            new.next=self.tail.next
            self.tail.next=new
        self.size+=1
    
    def addany(self,e,pos):
        new=node(e,None)
        p=self.head
        i=0
        while i<pos-1:
            p=p.next
            i+=1
        new.next=p.next
        p.next=new
        self.size+=1

    def removefirst(self):
        if self.isempty():
            print("circular linkedlist is empty")
            return
        e=self.head.data
        self.tail.next=self.head.next
        self.head=self.head.next
        if self.isempty():
            self.head=None
            self.tail=None
        return e

    def removelast(self):
        if self.isempty():
            print("circular linkedlist is empty")
            return
        p=self.head
        i=0
        while i<len(self)-1:
            p=p.next
            i+=1
        self.tail=p
        p=p.next
        self.tail.next=self.head
        e=p.data

        self.size-=1
    def removeany(self,pos):
        p=self.head
        i=0
        while i<pos-1:
            p=p.next
            i+=1
        a=p.next.data
        p.next=p.next.next
        self.size-=1
        return a
    def display(self):
        p=self.head
        i=0
        while i<len(self):
            print(p.data,end="-->")
            p=p.next
            i+=1
c=cir()
c.addfirst(10)
c.addfirst(20)
c.addfirst(30)
c.addlast(10)
c.addlast(20)
c.addany(40,2)
c.removefirst()
c.removelast()
c.removeany(2)
c.display()        