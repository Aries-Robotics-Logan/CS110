import random
import sys

def play_math_practice(number_of_problems, min_bound, max_bound):
    Counter = 1
    Points = 0
    correct = []
    incorrect = []
    while Counter <= number_of_problems:
        abc = random.randint(min_bound, max_bound)
        seco = random.randint(min_bound, max_bound)
        print(f"Question {Counter}: ")
        print(f"{abc} + {seco}")
        ans = abc + seco
        response = input("Answer: ")
        if int(response) == ans:
            Points += 1
            correct.append(f"{abc} + {seco}")
        else:
            incorrect.append(f"{abc} + {seco}")
        Counter += 1
    print(f"You Scored {Points} Points!")
    print(f"Correct Answers: {', '.join(correct)}")
    print(f"Incorrect Answers: {', '.join(incorrect)}")
    pass


if __name__ == '__main__':
    play_math_practice(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    #play_math_practice(10, 3, 99)
    pass
