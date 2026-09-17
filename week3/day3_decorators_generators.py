def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"Hello, {name}!"


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def func_name(function_name):
    return f"call {function_name}"


def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

@timer
def greet2():
    return "Hello!"


def require_positive(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 0:
            print("Error: argument must be positive")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_positive
def square(n):
    return n ** 2


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call #{wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def greet3():
    print("Hello!")


def count_down(n):
    i = n
    while i >= 1:
        yield i
        i -= 1


def even_numbers(limit):
    i = 0
    while i <= limit:
        if i % 2 == 0:
            yield i
        i += 1


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def read_lines_reversed(filename):
    with open(filename) as f:
        result = []
        for line in f:
            result.append(line.strip())
        index = len(result) - 1
        while index >= 0:
            yield result[index]
            index -= 1


def chunked(lst, size):
    i = 0
    while i < len(lst):
        yield lst[i:i+size]
        i += size


if __name__ == "__main__":
    print(greet("Anu"))
    print(func_name("addition"))
    print(greet2())
    print(square(5))
    print(square(-3))
    greet3()
    greet3()
    for val in count_down(3):
        print(val)
    for val in fibonacci(10):
        print(val)
    for chunk in chunked([1,2,3,4,5,6,7], 3):
        print(chunk)