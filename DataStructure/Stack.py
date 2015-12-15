# Implementation of Stack


class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1


    def push(self, item):
        if self.isfull():
            print("Sorry, the stack is full!")
        else:
            self.stack.append(item)
            self.top += 1

    def pop(self):
        if self.isempty():
            print("Sorry, it's a empty stack!")
        else:
            self.top -= 1
            return self.stack.pop()

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top + 1 == self.size


if __name__ == "__main__":
    aStack = Stack(4)
    aStack.push(1)
    aStack.push(2)
    aStack.push(3)
    aStack.push(4)

    for i in range(aStack.size):
        print(aStack.pop())


