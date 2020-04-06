# Author: Guðjón Ingi Valdimarsson
# Date: 26.03.2020

from enum import Enum

class OperationType(Enum):
    ADD = 1
    UPDATE = 2
    DELETE = 3

class OperationInfo:
    def __init__(self, type, data):
        self.type = type
        self.data = data

class InfoUndo():
    def __init__(self):
        self.stack = []
        self.dataStructure = {}

    def add(self, key, info):
        if key not in list(self.dataStructure):
            self.dataStructure[key] = info
        info = OperationInfo(OperationType.ADD, (key, info))
        self.stack.append(info)
    
    def update(self, key, info):
        if key in list(self.dataStructure):
            prev_info = self.dataStructure[key]
            self.dataStructure[key] = info
        info = OperationInfo(OperationType.UPDATE, (key, prev_info))
        self.stack.append(info)
    
    def delete(self, key):
        if key in list(self.dataStructure):
            info = OperationInfo(OperationType.DELETE, (key, self.dataStructure[key]))
            del self.dataStructure[key]
        self.stack.append(info)
    
    def undo(self):
        if len(self.stack) != 0:
            info = self.stack.pop()
            if info.type == OperationType.ADD:
                del self.dataStructure[info.data[0]]
            else:
                self.dataStructure[info.data[0]] = info.data[1]
        else:
            print ("No more operations to undo")
    
    def __str__(self):
        return str(self.dataStructure)

if __name__ == "__main__":
    ds = InfoUndo()
    ds.add(5, "hundur")
    ds.add(10, "Köttur")
    ds.update(5, "Hundur")
    print (ds)
    ds.undo()
    print (ds)
    ds.undo()
    print(ds)
    ds.undo()
    print(ds)
    ds.undo()
    print(ds)