class node :
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    def addlast(self,data):
        new=node(data,None)
        if self.isempty():
            self.head=new
        else:
            self.tail.next=new
        self.tail=new
        self.size+=1

    def push(self,data):
        new=node(data,None)
        new.next=self.head
        self.head=new

    def search(self,data):
        temp=self.head
        index=0
        while temp:
            if temp.data==data:
                return index
            temp=temp.next
            index+=1
        return -1

    def addfirst(self,data):
        new=node(data,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new

    def addany(self,data,p):
        new=node(data,None)
        temp=self.head
        i=1
        while i<p-1:
            temp=temp.next
            i+=1
        new.next=temp.next
        temp.next=new

    def removefirst(self):
        if self.isempty():
            print("list is empty")
            return
        a=self.head.data
        self.head=self.head.next
        if self.isempty():
            self.tail=None
        return a
        
    def removelast(self):
        if self.isempty():
            print("list is empty")
            return
        temp=self.head
        i=1
        while i<len(self)-1:
            self.temp=self.temp.next
            i+=1

        self.tail=temp
        temp=temp.next
        a=self.temp.data

    def removeany(self,p):
        temp=self.head
        i=1
        while i < p-1:
            temp=temp.next
            i+=1
        e=temp.next.data
        temp.next=temp.next.next
        return e
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
l=linkedlist()
l.addlast(10)
l.addlast(20)
l.addlast(30)
# l.display()
l.push(10)
l.push(20)
# l.display()
a=l.search(10)
print(a)
l.addfirst(50)
# l.display()
l.addany(70,4)
l.display()
print()
b=l.removefirst()
print(b)
ele=l.removeany(3)
l.display()

