class Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class QueuesLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self, element):
        newNode = Node(element, None)
        if self.isempty():
            self._front = newNode
        else:
            self._rear._next = newNode
        self._rear = newNode
        self._size += 1

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        element = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return element

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end='<--')
            p = p._next
        print()


# Q = QueuesLinked()
# Q.enqueue(5)
# Q.enqueue(3)
# Q.display()
# print('Length:', len(Q))
# Q.enqueue(7)
# Q.enqueue(12)
# Q.display()
# print('Length:', len(Q))
# print(Q.dequeue())
# Q.display()
# print('Length:', len(Q))
# print(Q.first())
