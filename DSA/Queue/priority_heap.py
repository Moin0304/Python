class heap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.csize = 0
    
    def __len__(self):
        return len(self.data)
    
    def isempty(self):
        return self.size == 0

    def insert(self,e):
        if self.csize == self.maxsize:
            print("no space in heap")
            return
        self.csize = self.csize + 1
        hi = self.csize
        while hi > 1 and e > self.data[hi//2]:
            self.data[hi] = self.data[hi//2]
            hi = hi//2
        self.data[hi] = e

    def max(self):
        if self.csize == 0:
            print("heap is empty")
            return
        return self.data[1]

    def deletemax(self):
        if self.csize == 0:
            print("heap is empty")
            return 
        e = self.data[1]
        self.data[1] = self.data[self.csize]
        self.data[self.csize] = -1
        self.csize = self.csize - 1
        i = 1
        j = i*2
        while j <= self.csize:
            if self.data[j] < self.data[j+1]:
                j = j+1
            if self.data[i] < self.data[j]:
                temp = self.data[i]
                self.data[i] = self.data[j]
                self.data[j] = temp
                i = j
                j = i*2
            else:
                break
        return e
 
s = heap()
s.insert(25)
s.insert(14)
s.insert(2)
s.insert(20)
s.insert(10)
print(s.data)
s.insert(40)
print(s.data)
s.deletemax()
print(s.deletemax())




