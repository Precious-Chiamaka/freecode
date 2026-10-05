def word_frequency(text):
    text = text.lower()

    cleaned = ''
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned += char

    words = cleaned.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_word = None
    most_count = 0
    for word, count in counts.items():
        if count > most_count:
            most_count = count
            most_word = word
    print(f"Most frequent word: {most_word} ({most_count})")

word_frequency("Python is fun, and Python is powerful!")
