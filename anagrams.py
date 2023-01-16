import random
import sys


def load_clues(filename):
    with open(filename) as file:
        return file.read().split('\n')


def word_scramble(word):
    size = len(word)
    list1 = random.sample(word, size)
    string33 = " ".join(list1)
    return string33


def play_anagrams(file):
    words = load_clues(file)
    word = random.choice(words)
    new_word = word_scramble(word)
    Counter = 1
    print(new_word)
    while True:
        response = input("Guess: ")
        if response == word:
            print('Correct!')
            print('Total Guesses: ' + str(Counter))
            return
        else:
            print("Incorrect")
            Counter += 1
    pass


if __name__ == '__main__':
    play_anagrams(sys.argv[1])
    pass
