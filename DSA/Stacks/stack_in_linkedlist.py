class stack:
    def __init__(self):
        self.data=[]
    
    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0
    
    def push(self,e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.data.pop()
    
    def top(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.data[-1]
s=stack()
s.push(1)
s.push(2)
s.push(3)
print(s.data)
print(s.pop())
print(s.top())
print(s.pop())
print(s.data)