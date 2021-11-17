class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def print_list(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def insert(self, index, value):
        if index > self.length:
            self.append(value)
        new_node = Node(value)
        leader_node = self.traverse_to_index(index-1)
        hold_pointer = leader_node.next
        leader_node.next = new_node
        new_node.next = hold_pointer
        self.length += 1

    def remove(self, index):
        leader_node = self.traverse_to_index(index-1)
        unwanted_node = leader_node.next
        leader_node.next = unwanted_node.next
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return self.head
        first_node = self.head
        self.tail = self.head
        second_node = first_node.next
        while second_node:
            temporary_value = second_node.next
            second_node.next = first_node
            first_node = second_node
            second_node = temporary_value
        self.head.next = None
        self.head = first_node


my_linked_list = SinglyLinkedList()
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.append(20)
my_linked_list.prepend(1)
my_linked_list.insert(1, 50)
my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.print_list()
print(my_linked_list)
