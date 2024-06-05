class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if  not self.isEmpty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.isEmpty():
            return self.items.peek[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit
       

    def search(self, target):
        if target in self.items:
            return self.items.index(target)
        else:
            raise ValueError("target not available")

