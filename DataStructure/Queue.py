# Implementation of Queue

class Queue:
    def __init__(self, size):
        self.__queue = []
        self.size = size

    def capacity(self):
        return len(self.__queue)


    def isfull(self):
        return len(self.__queue) == self.size


    def isempty(self):
        return len(self.__queue) == 0


    def enqueue(self, item):
        if self.isfull():
            print("The queue is full. Can't add any more!")
        else:
            self.__queue.append(item)

    def dequeue(self):
        if self.isempty():
            print("The queue is empty. No item to dequeue!")
        else:
            result = self.__queue[0]
            del self.__queue[0]
            return result

    def __hello__(self):
        return "Hello World"


if __name__ == "__main__":
    aQueue = Queue(6)
    print("Is queue empty: {0}".format(aQueue.isempty()))
    aQueue.enqueue(0)
    aQueue.enqueue(1)
    aQueue.enqueue(2)
    aQueue.enqueue(3)
    aQueue.enqueue(4)
    aQueue.enqueue(5)
    aQueue.enqueue(6)

    for i in range(aQueue.capacity()):
        print(aQueue.dequeue())

    print(aQueue.__hello__())

