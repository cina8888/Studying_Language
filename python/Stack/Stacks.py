class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.head is None:
            return "Stack is empty"
        
        popped_node = self.head
        self.size -= 1
        self.head = self.head.next
        return popped_node.value

    def traverseAndPrint(self):
        curNode = self.head
        while curNode:
            print(curNode.value, end =  " -> ")
            curNode = curNode.next
    

a = [1, 2, 3, 4, 5, 6, 7]
stack = Stack()
for x in a:
    stack.push(x)
print(stack.pop())
print(stack.traverseAndPrint())

        