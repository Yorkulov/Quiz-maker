from random import sample, shuffle
import os
import time


def quiz_generator(filename):
    words_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.split(',')
            word = [x.strip().lower() for x in word]
            words_list.append(word)
        return words_list


def print_quiz(words_list):
    count = 0
    shuffle(words_list)
    start_time = time.time()
    for word in words_list:
        choise_words = sample(words_list, 3)
        choise_words.append(word)
        shuffle(choise_words)
        print(f"\n\nWhat does it mean -> {word[1]}\n")
        print("-" * 50)
        for choise in choise_words:
            print(f"\t\t{choise[0]}")
        print("-" * 50)
        answer = input("\nEnter your answer: ")
        os.system('clear')
        if word[0] == answer:
            count += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"Your answer: {answer}")
            print(f"Correct answer: {word}")
    end_time = time.time()
    answer_time = end_time - start_time
    print(f"Your score: {count}")
    print(f"Mistake answer: {len(words_list) - count}")
    print(f"Your time {answer_time:.4f} seconds")

def main():
    words_list = quiz_generator("data.txt")
    print_quiz(words_list)



if __name__ == "__main__":
    main()