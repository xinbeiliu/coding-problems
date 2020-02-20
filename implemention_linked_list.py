class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, index, data):
        new_node = Node(data)
        current = self.head
        counter = 1
        while counter <= index:
            current = current.next
            counter += 1
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        current = self.head
        while current.next.data != data:
            current = current.next
        current.next = current.next.next

    def search(self, data):
        current = self.head
        while current.next is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        if self.head.next is None:
            return self.head
        current = self.head
        second = current.next

        while second is not None:
            temp = second.next
            second.next = current
            current = second
            second = temp

        self.head.next = None
        self.head = current

        return self.traverse()


my_ll = LinkedList()
my_ll.append('apple')
my_ll.append('berry')
my_ll.append('cherry')
my_ll.prepend('hello')
my_ll.insert(2, 'kale')
my_ll.remove('hello')
my_ll.remove('kale')
my_ll.traverse()
print(my_ll.search('kale'))
