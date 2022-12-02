class node:
    def __init__(self,data,next):
        self.data=data
        self.next=None

class link:
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
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
        self.size+=1

    def addlast(self,e):
        new=node(e,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new
        self.size+=1

    def addany(self,e,pos):
        new=node(e,None)
        temp=self.head
        i=0
        while i <pos-1:
            temp=temp.next
            i+=1
        p=temp
        new.next=temp.next
        temp.next=new
        self.size+=1

    def removefirst(self):
        if self.isempty():
            print("list is empty")
            return
        p=self.head
        self.head=self.head.next
        self.size-+1

    def removelast(self):
        if self.isempty():
            print("list is empty")
            return
        temp=self.head
        i=1
        while i<len(self)-1:
            temp=temp.next
            i+=1
        self.tail=temp
        self.tail.next=None
        self.size-=1

    def removeany(self,pos):
        temp=self.head
        i=0
        while i<pos-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        self.size-=1
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
l=link()
l.addfirst(10)
l.addfirst(20)
l.addfirst(30)
l.display()
print()
l.addlast(20)
l.addlast(30)
l.display()
print()
l.addany(10,2)
l.display()
print()
l.removefirst()
l.display()
print()
l.removelast()
l.display()
print()
l.removeany(2)
l.display()