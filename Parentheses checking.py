from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return None
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container)==0
    def display(self):
        return [x for x in self.container]

if __name__ == '__main__':
    a = Stack()
    f = 'Hi (this) {is}{} [Harish]!'
    for i in range(len(f)):
        a.push(f[i])
    print(a.display())

    x = Stack()
    for i in range(a.size()):
        if f[i] in '([{':
            x.push(f[i])
        elif f[i] in ')]}':
            if x.is_empty():
                x.push(f[i])
                break
            if f[i] == ')' and x.peek() == '(':
                x.pop()
            elif f[i] == '}' and x.peek() == '{':
                x.pop()
            elif f[i] == ']' and x.peek() == '[':
                x.pop()

    if x.is_empty():
        print('Balanced')
    else:
        print('Not Balanced')

    
