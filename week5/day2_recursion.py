def countdown(n):
    if n == 0:
        return []
    return [n] + countdown(n - 1)


def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:len(s) - 1])


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def binary_search(lst, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)


def subsets(lst):
    if len(lst) == 0:
        return [[]]
    first = lst[0]
    rest_subsets = subsets(lst[1:])
    with_first = []
    for s in rest_subsets:
        with_first.append([first] + s)
    return rest_subsets + with_first


if __name__ == "__main__":
    print(countdown(3))
    print(sum_to_n(4))
    print(power(2, 3))
    print(reverse_string("abc"))
    print(is_palindrome("racecar"))
    print(fibonacci(6))
    print(fibonacci_memo(50))
    print(count_digits(90210))
    print(flatten([1, [2, [3, 4]], 5]))
    print(binary_search([1, 3, 5, 7, 9], 7, 0, 4))
    print(subsets([1, 2]))