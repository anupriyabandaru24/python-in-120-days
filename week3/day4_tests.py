import pytest

def square(n):
    return n * n

def test_square():
    assert square(4) == 16


def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(4)
    assert not is_even(7)


def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def test_average():
    assert average(2, 4, 6) == 4.0
    assert average() == 0


def count_vowels(word):
    if len(word) == 0:
        return 0
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count += 1
    return count

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0


def remove_duplicates(lst):
    return list(set(lst))

def test_remove_duplicates():
    result = remove_duplicates([1, 2, 2, 3])
    assert len(result) == 3
    assert 1 in result
    assert 2 in result
    assert 3 in result


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

def test_counter():
    c = Counter()
    c.increment()
    c.increment()
    assert c.get_count() == 2


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == "Cannot divide by zero"


class Shape2:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

def test_shape2_area_not_implemented():
    s = Shape2("Generic")
    with pytest.raises(NotImplementedError):
        s.area()


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def test_fibonacci():
    result = list(fibonacci(5))
    assert result == [0, 1, 1, 2, 3]


def chunked(lst, size):
    i = 0
    while i < len(lst):
        yield lst[i:size+i]
        i += size

def test_chunked():
    result = list(chunked([1, 2, 3, 4, 5], 2))
    assert result == [[1, 2], [3, 4], [5]]