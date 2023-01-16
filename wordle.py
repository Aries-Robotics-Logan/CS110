import sys
import random

def wordle(infile, number):
    with open(infile) as file:
        word = random.choice(list(file))
    second_list = []
    for char in word:
        second_list.append(char)
    counter = 1
    while counter <= number:
        response = input("Guess # " + str(counter) + ": " +"\n")
        new_list = []
        for char in response:
            new_list.append(char)
        result = []
        for i in range(len(new_list)):
            if new_list[i] == second_list[i]:
                result.append("!")
            elif new_list[i] in word:
                result.append("?")
            else:
                result.append("*")
        edf = "".join(result)
        print(edf)
        counter += 1
        if new_list == second_list:
            break
    if new_list == second_list:
        print("Way to go!")
    else:
        print("Maybe next time. The answer is " + word + ".")



if __name__ == '__main__':
    wordle((sys.argv[1]), int(sys.argv[2]))

