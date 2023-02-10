"""Stack"""
class ArrayStacks:
    def __init__(self):
        self.data = []
    def size(self):
        return self.data.count()
    def is_empty(self):
        return True if len(self.data) == 0 else False
    def push(self, input_data):
        self.data.append(input_data)
    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            data = self.data[-1]
            self.data = self.data[:-1]
            return data
    def stackTop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            return self.data[-1]
    def printStack(self):
        print(*self.data, sep = ", ")

# myStack = ArrayStacks()
# myStack.push(10)
# myStack.push(20)
# myStack.push(30)
# y = myStack.stackTop()
# print(y)
# myStack.printStack()
# x = myStack.pop()
# print(x)
# myStack.pop()
# myStack.printStack()
# myStack.pop()
# print(myStack.is_empty())
# myStack.pop()