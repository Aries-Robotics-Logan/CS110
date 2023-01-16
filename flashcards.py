import random
import sys

def load_clues(filename):
    with open(filename) as file:
        return file.read().split('\n')


def flashcards(filename):
    Counter = 1
    Points = 0
    lines = load_clues(filename)
    shuffled_flashcards = random.sample(lines, len(lines))
    for line in shuffled_flashcards:
        question, ans = line.split("|")
        print(f"{question}")
        response = input("Guess: ")
        if response == ans:
            print("Correct!")
            Points += 1
        else:
            print("Incorrect.")
            print(f"Correct answer: {ans}")
    print(f"You got {Points}/{len(lines)} correct.")
    pass


if __name__ == '__main__':
    flashcards(sys.argv[1])
    pass
