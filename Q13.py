# 13. Write a program to compute the frequency of the words from the input. The
# output should output after sorting the key alphanumerically.

def word_frequency(words):
    word_freq = {}

    for word in words:
        current_freq = word_freq.get(word, 0)
        word_freq[word] = current_freq + 1

    sorted_word_freq = dict(sorted(word_freq.items()))
    return sorted_word_freq

def main():
    input_text = input("Enter string:\n")
    words = input_text.split()
    result = word_frequency(words)
    
    for word, freq in result.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
