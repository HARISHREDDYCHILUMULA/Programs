from collections import deque
class Queue:
    def __init__(self):
        self.container=deque()
    def enque(self,val):
        self.container.append(val)
    def deq(self):
        return self.container.popleft()
    def peek(self):
        if not self.is_empty():
            return self.container[0]
        else:
            return None
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container)==0
    def display(self):
        return [x for x in self.container]
