import random

# Make a word list from a text file
with open("wordlist_file.txt", "r") as file:
    read_file = file.readlines()
    word_list = []
    for line in range(1, (len(read_file))):
        word_list.append(read_file[(line - 1)])

# Function: Draw the character
def display(mistake_number, word_number, guessed_letters, balloon_list):
    for each_mistake in range(0, mistake_number):
        balloon_list[each_mistake] = "x"

    # Decorate the display
    if word_number == 0:
        other_word = ""
    elif word_number == 1:
        other_word = "Yes!"
    elif word_number == 2:
        pop_number = random.randint(1, 5)
        exclamation_number = random.randint(1, 3)
        other_word = " " * pop_number + "POP" + "!" * exclamation_number

    # Make the display
    print()
    print(f" {balloon_list[0]}  {balloon_list[1]}  {balloon_list[2]}")
    print(f"{balloon_list[3]} {balloon_list[4]}  {balloon_list[5]}  {balloon_list[6]}     {other_word}")
    print(f" {balloon_list[7]}  {balloon_list[8]}  {balloon_list[9]}")
    print(f"  \ | /            Your guesses:")
    print(f"   \|/  {guessed_letters}")
    print("    |")
    print("     \O")
    print("      |\ ")
    print("_____/_\___\n")

# Get different balloons
balloons = []
for ten_times in range(0, 10):
    balloon_random = random.randint(1, 2)
    if balloon_random == 1:
        balloons.append("O")
    else:
        balloons.append("o")

# Choose a word
chosen_word = random.choice(word_list)

# Make lists
word_as_list = []
for character in chosen_word:
    word_as_list.append(character.upper())

space = []
for character in range(0, len(chosen_word) - 1):
    if word_as_list[character] == "-":
        space.append("-")
    else:
        space.append("_")

# Set the variables
guesses_left = 10
not_won = True
not_lost = True
word_number_send = 0
guesses_so_far = ""

space_string = ""
for each_item in space:
    space_string += "  " + each_item

# Run the activity loop
while not_won and not_lost:
    display(10 - guesses_left, word_number_send, guesses_so_far, balloons)
    print(space_string)

    guess = (input("Choose a letter: ").upper())
    guesses_so_far += "  " + guess

    # Check if the guess is right/wrong
    if guess in word_as_list:
        for each_character in range(0, len(word_as_list)):
            if word_as_list[each_character] == guess:
                space[each_character] = guess
        word_number_send = 1
    else:
        guesses_left -= 1
        word_number_send = 2

    space_string = ""
    for each_item in space:
        space_string += "  " + each_item

    # Check win/lose conditions
    if "_" not in space:
        not_won = False
    if guesses_left == 0:
        not_lost = False

# Show win or loss
if not_lost == False:
    display(10 - guesses_left, 2, guesses_so_far, balloons)
    print(space_string)
    print(f"Sorry...  The word was: {chosen_word}")
else:
    display(10 - guesses_left, 1, guesses_so_far, balloons)
    print(space_string)
    print(f"You did it!  The word was: {chosen_word}")
