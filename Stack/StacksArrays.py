class StacksArrays():
    
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data[-1]


S = StacksArrays()
S.push(5)
S.push(3)
print(S._data)
print('Length', len(S))
print('Removed:', S.pop())
print(S.isempty())
print('Removed:', S.pop())
print(S.isempty())
S.push(7)
S.push(9)
S.push(4)
print(S._data)
print(S.top())
print(S._data)



