class node:
    def __init__(self, value):
        self.value = value
        self.next = None
class FloydAlgoritm:
    def view(self, root):
        if root is None:
            return "There is no Linked List"
        cur = root
        for _ in range(10):
            print(cur.value, end = " -> ")
            cur = cur.next
            if cur == None:
                print("None")
                return
        print("...")
        
    def FloydAL(self, head):
        if head is None:
            return
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        cur = slow
        while cur.next != slow:
            cur = cur.next
        cur.next = None
        
        
root = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)

root.next = node2
node2.next = node3
node3.next = node4
node4.next = root.next

do = FloydAlgoritm()
do.view(root)
do.FloydAL(root)
do.view(root)