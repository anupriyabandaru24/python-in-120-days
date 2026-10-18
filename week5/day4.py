class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 1. Python list -> linked list (returns the head)
def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        new_node = Node(v)
        current.next = new_node
        current = current.next
    return head


# 2. Linked list -> Python list
def to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.value)
        current = current.next
    return lst


# 3. Number of nodes
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


# 4. Add a node at the front (O(1)), returns the new head
def push_front(head, value):
    new = Node(value)
    new.next = head
    return new


# 5. Add a node at the end (O(n)), returns the head
def append(head, value):
    if not head:
        return Node(value)
    current = head
    while current.next:
        current = current.next
    current.next = Node(value)
    return head


# 6. Is the value in the list?
def contains(head, target):
    current = head
    while current:
        if current.value == target:
            return True
        current = current.next
    return False


# 7. Delete the first node with this value, returns the head
def delete_value(head, target):
    if not head:
        return None
    if head.value == target:
        return head.next
    current = head
    while current.next:
        if current.next.value == target:
            current.next = current.next.next
            return head
        current = current.next
    return head


# 8. Reverse in place, returns the new head
def reverse(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


# 9. Middle value with slow/fast pointers
def middle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value


# 10. Cycle detection (Floyd's tortoise and hare)
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    print(to_list(build_list([1, 2, 3])))
    print(length(build_list([1, 2, 3])), length(None))
    print(to_list(push_front(build_list([2, 3]), 1)))
    print(to_list(append(build_list([1, 2]), 3)), to_list(append(None, 5)))
    print(contains(build_list([1, 2, 3]), 2), contains(build_list([1, 2, 3]), 5))
    print(to_list(delete_value(build_list([1, 2, 3]), 1)))
    print(to_list(delete_value(build_list([1, 2, 3]), 2)))
    print(to_list(delete_value(build_list([1, 2, 3]), 3)))
    print(to_list(delete_value(build_list([1, 2, 3]), 9)))
    print(to_list(delete_value(build_list([1, 2, 1]), 1)))
    print(to_list(reverse(build_list([1, 2, 3]))), to_list(reverse(None)))
    print(middle(build_list([1, 2, 3, 4, 5])), middle(build_list([1, 2, 3, 4])), middle(None))
    a = build_list([1, 2, 3])
    print(has_cycle(a))
    a.next.next.next = a
    print(has_cycle(a))
    b = build_list([1, 2, 3, 4])
    b.next.next.next = b.next
    print(has_cycle(b))
    c = build_list([1])
    c.next = c
    print(has_cycle(c), has_cycle(None))