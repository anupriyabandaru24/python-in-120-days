from collections import deque


# 1. Reverse a string with a stack
def reverse_with_stack(s):
    stack = list(s)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result)


# 2. Stack class (LIFO)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# 3. Queue class (FIFO)
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# 4. Sort by length, then alphabetically
def sort_by_length(words):
    return sorted(words, key=lambda w: (len(w), w))


# 5. Marks high to low, ties by name A to Z
def rank_students(students):
    return sorted(students, key=lambda s: (-s["marks"], s["name"]))


# 6. Bubble sort (in place, with early exit)
def bubble_sort(lst):
    if len(lst) <= 1:
        return lst
    for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            return lst
    return lst


# 7. Balanced parentheses (one type)
def is_balanced(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif not stack:
            return False
        else:
            stack.pop()
    return not stack


# 8. Valid brackets (three types)
def is_valid(s):
    stack = []
    pairs = {"}": "{", "]": "[", ")": "("}
    for ch in s:
        if ch in "{[(":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


# 9. Postfix calculator
def eval_postfix(tokens):
    stack = []
    for t in tokens:
        if t == "+":
            r = stack.pop()
            l = stack.pop()
            stack.append(l + r)
        elif t == "-":
            r = stack.pop()
            l = stack.pop()
            stack.append(l - r)
        elif t == "*":
            r = stack.pop()
            l = stack.pop()
            stack.append(l * r)
        elif t == "/":
            r = stack.pop()
            l = stack.pop()
            stack.append(l // r)
        else:
            stack.append(int(t))
    return stack[0]


# 10. Queue built from two stacks
class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.in_stack and not self.out_stack:
            raise IndexError("Stacks are empty")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


if __name__ == "__main__":
    print(reverse_with_stack("hello"))
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek(), s.pop(), s.size(), s.is_empty())
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print(q.dequeue(), q.size())
    print(sort_by_length(["pear", "fig", "apple", "kiwi"]))
    print(rank_students([
        {"name": "Ravi", "marks": 90},
        {"name": "Anu", "marks": 90},
        {"name": "Sam", "marks": 75},
    ]))
    print(bubble_sort([5, 2, 9, 1]))
    print(is_balanced("(())"), is_balanced(")("))
    print(is_valid("{[()]}"), is_valid("(("))
    print(eval_postfix(["2", "3", "+", "4", "*"]), eval_postfix(["7", "2", "-"]))
    qs = QueueWithStacks()
    qs.enqueue("a")
    qs.enqueue("b")
    print(qs.dequeue())
    qs.enqueue("c")
    print(qs.dequeue(), qs.dequeue())