class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newNode = _Node(e, None)
        if self.isempty():
            newNode._next = newNode
            self._head = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def addfirst(self, element):
        newNode = _Node(element, None)
        if self.isempty():
            self._tail = newNode
            newNode._next = newNode
        else:
            newNode._next = self._head
            self._tail._next = newNode
        self._head = newNode
        self._size += 1

    def addany(self, element, position):
        newNode = _Node(element, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        newNode._next = p._next
        p._next = newNode
        self._size += 1

    def removefirst(self):
        if(self.isempty()):
            print('List is empty')
            return
        ele = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
        return ele

    def removelast(self):
        if(self.isempty()):
            print('List is empty')
            return
        ele = self._tail._element
        p = self._head
        i = 1
        while i < self._size - 1:
            p = p._next
            i += 1
        self._tail = p
        self._tail._next = self._head
        self._size -= 1
        return ele

    def removeany(self, position):
        if self.isempty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        return ele


    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()

C = CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.display()
print('Size:', len(C))
C.addlast(8)
C.addlast(3)
C.display()
print('Size:', len(C))
# C.addfirst(25)
# C.display()
# print('Size:', len(C))
# C.addfirst(35)
# C.display()
# print('Size:', len(C))
# C.addany(20, 3)
# C.display()
# print('Size:', len(C))
# C.addany(30, 6)
# C.display()
# print('Size:', len(C))
# ele = C.removefirst()
# C.display()
# print('Size:', len(C))
# print('Element removed:', ele)
# ele = C.removefirst()
# C.display()
# print('Size:', len(C))
# print('Element removed:', ele)
# ele = C.removelast()
# C.display()
# print('Size:', len(C))
# print('Element removed:', ele)
# ele = C.removelast()
# C.display()
# print('Size:', len(C))
# print('Element removed:', ele)

ele = C.removeany(3)
C.display()
print('Size:', len(C))
print('Element removed:', ele)
ele = C.removeany(2)
C.display()
print('Size:', len(C))
print('Element removed:', ele)