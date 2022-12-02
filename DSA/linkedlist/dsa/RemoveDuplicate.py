class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def remove_duplicate(self):
        head=None
        tail=None
        dup=None
        head=self.head
        while head !=None and head.next !=None:
            tail=head
            while tail.next !=None:
                if head.data == tail.next.data:
                    dup =tail.next
                    tail.next = tail.next.next
                else:
                    tail = tail.next
                head=head.next
    
    def display(self):
        temp=self.head
        while temp != None:
            print(temp.data, end=' ')
            temp=temp.next
        print()

l=linkedlist()
# temp=l.head
temp=cur=node(0)
# for i in range (10):
#     n=node(int(input()))
#     temp.next=n
#     temp=temp.next
# l.head=cur.next
l.head=node(1)
l.head.next=node(2)
l.head.next.next=node(3)
l.head.next.next.next=node(3)
l.head.next.next.next.next=node(4)
l.head.next.next.next.next.next=node(5)
print('linked list before removing duplicate: ')
print()
l.display()
l.remove_duplicate()
print()
print('linked list after removing duplicate: ')
l.display()
