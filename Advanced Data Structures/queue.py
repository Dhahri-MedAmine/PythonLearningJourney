class Queue:
    def __init__(self, queue=None) -> None:
        self.__queue = queue if queue is not None else []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0) if self.__queue else None

    def front(self):
        return self.__queue[0] if self.__queue else None

    def is_Empty(self):
        return not self.__queue

    def size(self):
        return len(self.__queue)


def hotPotato(names, passes):
    children = Queue(names)
    last_child = ""
    while children.size() > 1:
        last_child = children.front()
        for p in range(passes):
            children.enqueue(children.dequeue())
        children.dequeue()

    return last_child


children = ["Bob", "John", "Emily", "Clara", "3entit", "Rosy"]
print(hotPotato(children, 10))
