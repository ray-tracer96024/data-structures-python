class linkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    # Push into the linked list
    def insertNodeAtStart(self, data):
        newNode = linkedListNode(data)
        newNode.next = self.head
        self.head = newNode

    # Insert after a node
    def insertNodeAfter(self, previousNode, data):
        if previousNode is None:
            print('The previous node is none...\nExiting...')
            exit()

        newNode = linkedListNode(data)
        newNode.next = previousNode.next
        previousNode.next = newNode

    # Insert at the end aka append
    def insertNodeAtEnd(self, data):
        newNode = linkedListNode(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    # Delete node
    def deleteNode(self, value):
        store = self.head
        if store is not None:
            if store.data == value:
                self.head = store.next
                store = None
                return

        while store is not None:
            if store.data == key:
                break

            previous = store
            store = store.next

        if store == None:
            return

        previous.next = store.next
        store = None

    # Print node
    def printLL(self):
        store = self.head
        while store:
            print(store.data, end = ' ')
            store = store.next
        print()

def main():
    ll = linkedList()
    ll.insertNodeAtStart(10)
    ll.insertNodeAtStart(20)
    ll.insertNodeAtStart(30)
    ll.insertNodeAtStart(40)
    # ll.insertNodeAfter(ll.head.next, 50)
    ll.insertNodeAtStart(60)
    ll.insertNodeAtEnd(70)
    ll.insertNodeAtStart(80)
    ll.insertNodeAtStart(90)
    ll.insertNodeAtStart(100)

    print('The linked list is: ', end = ' ')
    ll.printLL()
    ll.deleteNode(100)
    print('The linked list is: ', end = ' ')
    ll.printLL()

if __name__ == '__main__':
    main()
