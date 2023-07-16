class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head == None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def remove_from_back(self):
        if self.head == None:
            return None
        if self.head.next == None:
            value = self.head.value
            self.head = None
            return value
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        value = runner.next.value
        runner.next = None
        return value

    def remove_val(self, val):
        if self.head == None:
            return None
        if self.head.value == val:
            return self.remove_from_front()
        runner = self.head
        while runner.next != None:
            if runner.next.value == val:
                value = runner.next.value
                runner.next = runner.next.next
                return value
            runner = runner.next
        return None

    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        runner = self.head
        while runner != None and n > 1:
            runner = runner.next
            n -= 1
        if runner == None:
            return self.add_to_back(val)
        new_node = SLNode(val)
        new_node.next = runner.next
        runner.next = new_node
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None



"""



Let's explain each new method:

remove_from_front(self):

Check if the list is empty by verifying if self.head is None.
If the list is empty, return None.
Otherwise, store the value of the first node in a variable called value.
Update self.head to the next node.
Return the stored value.
remove_from_back(self):

Check if the list is empty by verifying if self.head is None.
If the list is empty, return None.
Check if there is only one node in the list by verifying if self.head.next is None.
If there is only one node, store its value in a variable called value, set self.head to None, and return the stored value.
If there are more than one nodes, iterate over the list until the second-to-last node (runner.next.next is None).
Store the value of the last node in a variable called value.
Set the next attribute of the second-to-last node to None.
Return the stored value.
remove_val(self, val):

Check if the list is empty by verifying if self.head is None.
If the list is empty, return None.
Check if the value to be removed is in the first node (self.head.value == val).
If it is in the first node, call remove_from_front() to remove and return the value.
Iterate over the list until the second-to-last node (runner.next is None).
Check if the value to be removed is in the next node (runner.next.value == val).
If it is in the next node, store its value in a variable called value, and update the next attribute of the current node to skip the next node (runner.next = runner.next.next).
Return the stored value.
insert_at(self, val, n):

Check if n is 0. If it is, call add_to_front(val) to insert the value at the beginning of the list.
Iterate over the list until the nth node or the end of the list is reached.
If the end of the list is reached (runner is None), call add_to_back(val) to insert the value at the end of the list.
Otherwise, create a new node with the given value.
Update the next attribute of the new node to point to the next node (new_node.next = runner.next).
Update the next attribute of the current node to point to the new node (runner.next = new_node).
Return self.
These modifications allow the SList class to remove nodes from the front and back, remove nodes with specific values, and insert nodes at specific positions.
"""

my_list = SList()

# Adding nodes to the list
my_list.add_to_front("are")
my_list.add_to_front("Linked lists")
my_list.add_to_back("fun!")

# Printing the values of the list
my_list.print_values()
# Output: Linked lists, are, fun!

# Removing the first node and printing its value
removed_value = my_list.remove_from_front()
print("Removed value:", removed_value)
# Output: Removed value: Linked lists

# Removing the last node and printing its value
removed_value = my_list.remove_from_back()
print("Removed value:", removed_value)
# Output: Removed value: fun!

# Removing a node with a specific value and printing its value
removed_value = my_list.remove_val("are")
print("Removed value:", removed_value)
# Output: Removed value: are

# Printing the updated list after removals
my_list.print_values()
# Output: (Empty list)

# Inserting a node at the beginning of the list
my_list.insert_at("Hello", 0)
my_list.print_values()
# Output: Hello

# Inserting a node at the end of the list
my_list.insert_at("World", 1)
my_list.print_values()
# Output: Hello, World

# Inserting a node in the middle of the list
my_list.insert_at("Awesome", 1)
my_list.print_values()
# Output: Hello, Awesome, World
