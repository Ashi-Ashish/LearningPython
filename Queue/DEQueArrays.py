class DEQueArrays:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self, element):
        self._data.insert(0, element)

    def addlast(self, element):
        self._data.append(element)

    def removefirst(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[-1]

D = DEQueArrays()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
print(D._data)
print('Length:', len(D))
print(D.removefirst())
print(D.removelast())
print(D._data)
print(D.first())
print(D.last())
