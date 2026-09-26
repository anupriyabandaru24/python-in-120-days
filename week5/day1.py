def find_max(lst):
    largest = lst[0]
    for i in range(len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


def reverse_string(s):
    i = len(s) - 1
    re_string = ""
    while i >= 0:
        re_string += s[i]
        i -= 1
    return re_string


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def contains_duplicate(lst):
    set_duplicates = set()
    for i in lst:
        if i in set_duplicates:
            return True
        set_duplicates.add(i)
    return False


def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - nums[i]], i]
        seen[nums[i]] = i


def first_unique_char(s):
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1


def most_frequent(lst):
    count = {}
    for i in lst:
        count[i] = count.get(i, 0) + 1
    best_item = None
    best_count = 0
    for item, freq in count.items():
        if freq > best_count:
            best_count = freq
            best_item = item
    return best_item


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for i in range(len(s1)):
        count[s1[i]] = count.get(s1[i], 0) + 1
        count[s2[i]] = count.get(s2[i], 0) - 1
    for val in count:
        if count[val] != 0:
            return False
    return True


def max_subarray_sum(nums, k):
    sum_subarray = 0
    max_sum = 0
    for i in range(k):
        sum_subarray += nums[i]
        max_sum = sum_subarray
    for i in range(k, len(nums)):
        sum_subarray += nums[i]
        sum_subarray = sum_subarray - nums[i - k]
        max_sum = max(max_sum, sum_subarray)
    return max_sum


def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = "".join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())


if __name__ == "__main__":
    print(find_max([3, 7, 2, 9, 4]))
    print(reverse_string("hello"))
    print(is_palindrome("racecar"))
    print(is_palindrome("Aba"))
    print(contains_duplicate([1, 2, 3, 2]))
    print(two_sum([2, 7, 11, 15], 9))
    print(first_unique_char("leetcode"))
    print(most_frequent([1, 3, 2, 3, 4, 3, 2]))
    print(is_anagram("listen", "silent"))
    print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))