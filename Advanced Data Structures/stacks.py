from inspect import stack


class Stack:
    def __init__(self, stack=None) -> None:
        self.__stack = stack if stack is not None else []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop() if self.__stack else None

    def peek(self):
        return self.__stack[-1] if self.__stack else None

    def is_Empty(self):
        return not self.__stack

    def size(self):
        return len(self.__stack)

    def __str__(self) -> str:
        return str(self.__stack)


def reverse_word(word):
    stack = Stack(list(word))
    reversed = ""
    while not stack.is_Empty():
        reversed += str(stack.pop())
    return reversed


word = input("Please provide a word: ")

reversed = reverse_word(word)

print(f"Reverse of '{word}' is: '{reversed}'")
