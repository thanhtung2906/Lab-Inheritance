class Stack:
    def __init__(self) -> None:
        self.data = []
    def push(self,data):
        self.data.insert(0,data)
    def pop(self):
        return self.data.pop(0)
    def peek(self):
        return  self.data[0]
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
Tung = Stack()
Tung.push(1)
Tung.push(2)
Tung.push(3)
Tung.push(4)
Tung.push(5)
Tung.push(6)
Tung.push(12)

print(Tung.pop()) 
print(Tung.peek())
print(Tung.is_empty())  
