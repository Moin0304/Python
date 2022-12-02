class node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
class que:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    # def queue(self,e):
    #     new=node(e,None)
    #     if self.isempty():
    #         self.head=new
    #         self.tail=new
    #     else:
    #         self.tail.next=new
    #         new.next=None
    #         self.tail=new
    #     self.size+=1

    # def deque(self):
    #     if self.isempty():
    #         print("deque is empty")
    #         return
    #     self.head=self.head.next
    #     self.size-=1

    def queue(self,e):
        new=node(e,None)
        if self.isempty():
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
        self.size+=1

    def deque(self):
        if self.isempty():
            print("list is empty")
            return
        temp=self.head
        i=1
        while i<len(self)-1:
            temp=temp.next
            i+=1

        self.tail=temp
        temp=temp.next


    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end='-->')
            temp=temp.next
q=que()
q.queue(10)
q.queue(20)
q.queue(30)
q.display()
print()
q.deque()
q.display()