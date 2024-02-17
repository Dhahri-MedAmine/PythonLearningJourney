from typing import Optional


class EmptyList(Exception):
    pass


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next: Node = self
        self.previous: Node = self

    def flip(self):
        self.next, self.previous = (self.previous, self.next)

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"prev: {self.previous} - data: {self.data} - next: {self.next}"


class CircularDoublyLinkedLists:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    @property
    def is_empty(self):
        return self.head is None or self.tail is None

    def append(self, data):
        new_node = Node(data)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            new_node.previous = self.tail
            self.tail.next = new_node
            self.head.previous = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        new_node.previous = self.tail
        self.head.previous = new_node
        self.tail.next = new_node
        self.head = new_node

    def insert(self, key, data):

        if self.head is None or self.tail is None:
            raise EmptyList

        if self.tail.data == key:
            self.append(data)
            return

        current_node = self.head
        while True:
            if current_node.data == key:
                new_node = Node(data)
                new_node.previous = current_node
                new_node.next = current_node.next
                current_node.next = new_node
                new_node.next.previous = new_node
                return

            if current_node == self.tail:
                raise KeyError(key)

            current_node = current_node.next

    def delete(self, key):
        if self.head is None or self.tail is None:
            raise EmptyList

        if self.head.data == key:
            self.tail.next = self.head.next
            self.head.next.previous = self.tail
            self.head = self.head.next
            return

        if self.tail.data == key:
            self.tail.previous.next = self.head
            self.head.previous = self.tail.previous
            self.tail = self.tail.previous
            return

        current_node = self.tail
        while True:
            if current_node.data == key:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous
                return

            if current_node == self.head:
                raise KeyError(key)

            current_node = current_node.previous

    def update(self, key, data):
        if self.head is None or self.tail is None:
            raise EmptyList

        current_node = self.head
        while True:
            if current_node.data == key:
                current_node.data = data
                return

            if current_node == self.tail:
                raise KeyError(key)
            current_node = current_node.next

    def search(self, key):
        if self.head is None or self.tail is None:
            return None

        current_node = self.head
        while True:
            if current_node.data == key:
                return current_node
            if current_node == self.tail:
                return None
            current_node = current_node.next

    def reverse(self):
        if self.head is None or self.tail is None:
            return

        if self.head == self.tail:
            return

        current_node = self.head
        next_node = current_node.next
        while True:
            current_node.flip()
            if current_node == self.tail:
                break

            current_node = next_node
            next_node = current_node.next

        self.head, self.tail = self.tail, self.head

    def display(self):
        if self.head is None or self.tail is None:
            print(None)
            return

        current_node: Node = self.head
        while True:
            if current_node == self.tail:
                print(f"{current_node.data:02}")
                return
            else:
                print(f"{current_node.data:02}", end=" -> ")
                current_node = current_node.next

    def display_head_tail(self):
        if self.is_empty:
            print(None)
            return

        print(f"head: '{self.head}' - tail: '{self.tail}'")

if __name__ == "__main__":
    linked_list = CircularDoublyLinkedLists()
    # [linked_list.append(i) for i in range(11)]
    [linked_list.append(name) for name in ["Bob", "Joe", "Jane", "Jill", "Jack", "Jessie", "Jake"]]
    linked_list.display()
    linked_list.display_head_tail()

    linked_list.delete("Jake")
    linked_list.reverse()
    linked_list.display()
    linked_list.display_head_tail()
