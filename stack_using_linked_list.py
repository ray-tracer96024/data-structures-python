class stackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class stackUsingLL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def pushToStack(self, data):
        if self.head == None:
            self.head = stackNode(data)
        else:
            newNode = stackNode(data)
            newNode.next = self.head
            self.head = newNode

    def popFromStack(self):
        if self.isEmpty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return poppedNode.data

    def peekTopOfStack(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data

    def printStack(self):
        temporary = self.head
        if self.isEmpty():
            return None

        while(temporary != None):
            print(temporary.data, end = ' ')
            temporary = temporary.next
        return

def main():
    s = stackUsingLL()
    s.pushToStack(10)
    s.pushToStack(20)
    s.pushToStack(30)
    s.pushToStack(40)
    s.pushToStack(50)
    s.pushToStack(60)
    print('The stack is: ', end = ' ')
    s.printStack()
    print()
    s.popFromStack()
    print('The stack after popping is: ', end = ' ')
    s.printStack()
    print()

if __name__ == '__main__':
    main()
