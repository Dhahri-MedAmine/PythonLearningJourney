from typing import Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Data: {self.data} - Next: {self.next}"

    def __str__(self) -> str:
        return f"{self.data}"


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        previous_node = self.head
        current_node = previous_node.next
        while current_node:
            if current_node.data == key:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

        print("No Item found.")

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def insert(self, key, data):
        if self.head is None:
            print("List is empty.")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

        print("No item found.")

    def update(self, key, new_data):
        if self.head is None:
            print("List is empty.")
            return
        
        current_node = self.head
        while current_node:
            if current_node.data == key:
                current_node.data = new_data
                return
            current_node = current_node.next

        print("Item not found")

    def display(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data:02}", end=" -> ")
            current_node = current_node.next
        print("None")


linked_list = SinglyLinkedList()
[linked_list.append(i) for i in range(11)]

linked_list.display()
linked_list.update(5, "XX")
linked_list.display()
