def clean_text(text):
    text = text.lower()
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace(',', '')
    text = text.replace('?', '')
    return text


def count_words(text):
    words = text.split()
    count = {}
    for wrd in words:
        count[wrd] = count.get(wrd, 0) + 1
    return count


def top_n_words(word_counts, n):
    list_of_sort = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return list_of_sort[:n]


with open("sample.txt", "r") as f:
    text = f.read()
cleaned = clean_text(text)
counts = count_words(cleaned)
top_words = top_n_words(counts, 5)
for word, count in top_words:
    print(f"{word}: {count}")