import random

with open("wordlist_file.txt", "r") as file:
    read_file = file.readlines()
    word_list = []
    for line in range(1, (len(read_file))):
        word_list.append(read_file[(line - 1)])

def display(mistake_number, word_number, guessed_letters):
    guess_box_1 = "O"
    guess_box_2 = "o"
    guess_box_3 = "O"
    guess_box_4 = "o"
    guess_box_5 = "O"
    guess_box_6 = "o"
    guess_box_7 = "o"
    guess_box_8 = "o"
    guess_box_9 = "O"
    guess_box_10 = "O"    

    if mistake_number >= 1:
        guess_box_1 = "x"
        if mistake_number >= 2:
            guess_box_2 = "x"
            if mistake_number >= 3:
                guess_box_3 = "x"
                if mistake_number >= 4:
                    guess_box_4 = "x"
                    if mistake_number >= 5:
                        guess_box_5 = "x"
                        if mistake_number >= 6:
                            guess_box_6 = "x"
                            if mistake_number >= 7:
                                guess_box_7 = "x"
                                if mistake_number >= 8:
                                    guess_box_8 = "x"
                                    if mistake_number >= 9:
                                        guess_box_9 = "x"
                                        if mistake_number >= 10:
                                            guess_box_10 = "x"
    your_guesses = "Your guesses:"
    if word_number == 0:
        other_word = ""
    elif word_number == 1:
        other_word = "  Yes!"
    elif word_number == 2:
        pop_number = random.randint(1,2)
        if pop_number == 1:
            other_word = "POP!"
        else:
            other_word = "    POP!"
    print()
    print(f" {guess_box_1}  {guess_box_2}  {guess_box_3}")
    print(f"{guess_box_4} {guess_box_5}  {guess_box_6}  {guess_box_7}    {other_word}")
    print(f" {guess_box_8}  {guess_box_9}  {guess_box_10}")
    print(f"  \ | /           {your_guesses}")
    print(f"   \|/  {guessed_letters}")
    print("    |")
    print("     \O")
    print("      |\ ")
    print("_____/_\___")

chosen_word = random.choice(word_list)
space = []
for char in range(1, len(chosen_word)):
    space.append("_ ")
word_as_list = []
for char in chosen_word:
    word_as_list.append(char + " ")
guesses_left = 10
not_won = True
not_lost = True
word_number_send = 0
my_guesses = ""
while not_won and not_lost:
    display(10 - guesses_left, word_number_send, my_guesses)
    print(space)
    guess = (input("Choose a letter: ").lower() + " ")
    my_guesses = my_guesses + " " + guess
    if guess in word_as_list:
        for list_member in range(0, len(word_as_list)):
            if word_as_list[list_member] == guess:
                space[list_member] = guess
        word_number_send = 1
    else:
        guesses_left -= 1
        word_number_send = 2
    if "_ " not in space:
        not_won = False
    if guesses_left == 0:
        not_lost = False

if not_lost == False:
    display(10 - guesses_left, 0, my_guesses)
    print(space)
    print(f"Sorry...  The word was: {chosen_word}")
else:
    display(10 - guesses_left, 0, my_guesses)
    print(space)
    print(f"You did it!  The word was: {chosen_word}")
