"""
Word Occurrences
Estimate: 30 minutes
Actual:   69 minutes
"""

def count_word_occurrences(text):
    """Count occurrences of words in a string."""
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    for word, count in sorted(word_counts.items()):
        print(f"{word} : {count}")

if __name__ == "__main__":
    main()

#AFTER THE HINT
"""
Word Occurrences
Estimate: 25 minutes
Actual:   34 minutes
"""


def count_word_occurrences(text):
    """Count occurrences of words in a string."""
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)

    # Determine the maximum width needed for formatting
    max_width = max(len(word) for word in word_counts.keys())

    # Print the sorted word counts with aligned formatting
    for word in sorted(word_counts):
        print(f"{word:{max_width}} : {word_counts[word]}")


if __name__ == "__main__":
    main()
