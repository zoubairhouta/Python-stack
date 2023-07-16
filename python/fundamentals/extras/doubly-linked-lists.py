# with help of the internet to use after to reread 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                else:
                    self.head = current.next
                    if current.next:
                        current.next.prev = None
                break
            current = current.next

    def insert_node(self, data, before_data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == before_data:
                if current.prev:
                    current.prev.next = new_node
                    new_node.prev = current.prev
                else:
                    self.head = new_node
                new_node.next = current
                current.prev = new_node
                break
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def is_circular(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def remove_duplicates(self):
        current = self.head
        unique_values = set()

        while current:
            if current.data in unique_values:
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
            else:
                unique_values.add(current.data)

            current = current.next

    def reverse_list(self):
        current = self.head
        prev_node = None

        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node

        self.head = prev_node