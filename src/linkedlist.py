class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create Nodes
node1 = Node(15)
node2 = Node(45)
node3 = Node(32)

# Link nodes
node1.next = node2
node2.next = node3

# head points to node
head = node1

current = head
while current:
    print(current.data, end="-->")
    current = current.next
print("None")
