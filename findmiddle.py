
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.size = 0
        self.head = head

    def insertNode(self, value):
        node = Node(value)
        print(node)
        if self.head == None:
            node = self.head
            return
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.next is None:
                    currentNode.next = node
                    break
                else:
                    currentNode = currentNode.next

    def printList(self):
        currentNode = self.head
        while currentNode:
            print (currentNode.value)
            currentNode = currentNode.next
        

    def findMiddleElement(self):
        slow_pntr = self.head
        fast_pntr = self.head
        if self.head is not None:
            while fast_pntr is not None and fast_pntr.next is not None:
                fast_pntr = fast_pntr.next.next
                slow_pntr = slow_pntr.next
            print ("Here is the middle element", slow_pntr.value)

            
LL = LinkedList()
LL.insertNode(5)
LL.insertNode(20)
LL.insertNode(96)
LL.insertNode(67)
LL.insertNode(34)
LL.printList()
LL.findMiddleElement()

            
