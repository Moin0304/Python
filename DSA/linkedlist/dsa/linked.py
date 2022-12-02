class _Node:
    __slots__ = "_element","_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next

class Linked_List:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_last(self,e):
        newest = _Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def add_first(self,e):
        newest = _Node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def addany(self,e,position):
        newest = _Node(e,None)
        p = self._head
        i=1
        if self.is_empty():
            self._head = newest
            self._tail = newest
        elif self.__len__() < position:
            self._tail._next = newest
            self._tail = newest
        elif position == 1:
            self.add_first(e)
        else:
            while i < position-1:
                p = p._next
                i += 1
            newest._next = p._next
            p._next = newest
        self._size += 1    

    def deletefirst(self):
        if self.is_empty():
            return "Linked list is empty"
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        self._size -= 1

    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    def display(self):
        p = self._head
        while p:
            print(p._element,end="-->")
            p = p._next
        print()


l = Linked_List()
l.add_last(5)
l.add_last(6)
l.add_last(8)
l.add_last(1)
l.add_last(10)
l.add_last(12)
l.add_last(52)

l.display()
print(len(l))

l.add_first(9)
l.add_first(3)

l.display()
print(len(l))

print("index :",l.search(12))

l.addany(100,10)
l.display()
l.deletefirst()
l.display()