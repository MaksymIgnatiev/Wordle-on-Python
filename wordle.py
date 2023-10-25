import random
import requests
Word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(Word_site)
WORDS = response.content.splitlines()
letters = "abcdefghijklmnopqrstuvwxyz"
def mainLoop():
    global game_won, attempts, attempts_passed, random_word
    random_word = random.choice(WORDS).decode("utf-8")
    while len(random_word) >= 8:
      random_word = random.choice(WORDS).decode("utf-8")
    same_words = len([s_word.decode("utf-8") for s_word in WORDS if len(s_word) == len(random_word)])
    letters_tryed, some_letters = [], []
    correct_letters = ["_"] * len(random_word)
    word_field = ["_" * len(random_word) ] * 10
    attempts = 10
    attempts_passed = 0
    game_won = False
    word_guessed = False

    print(f"\nThis time the word is {len(random_word)} letters lenght")
    print(f"There are {same_words} words that has {len(random_word)} letters lenght")

    #hg main game loop
    while not word_guessed:
        if attempts_passed < attempts:

            #hg display different information
            if letters_tryed != []:
                print(f"There are no letters at all: {', '.join(letters_tryed)}")
            if some_letters != []:
                print(f"Some letters guessed: {', '.join(some_letters)}")
            if correct_letters != ["_"] * len(random_word):
              print(f"Correct letters: \" {' '.join(correct_letters)} \"")
            if word_field[0] != "_" * len(random_word):
                print(f"List of all tryed words:")
                print(f"↓" * len(word))
                for i in range(len(word_field)):
                    print(f"{word_field[i]}")
                print(" ")
            print(f"You have {attempts - attempts_passed} attempts left.")

            word_input = input("Your word: ") #g! ask for a word
            print(" ")
            word = word_input.lower()
            if word == random_word:
                word_guessed = True
                for i in range(len(word)):
                    letter = word[i]
                    if letter in letters:
                        if letter not in letters_tryed and letter not in random_word and word[i] != random_word[i]:
                            letters_tryed.append(letter)

                        if letter in random_word:
                            if letter not in some_letters:
                                some_letters.append(letter)
                            if word[i] == random_word[i]:
                                correct_letters[i] = letter
                    else:
                        print(f"There are no {letter} letter in english alphabet. Please try again")
                        break
                word_field[attempts_passed] = word
                game_won = True
                attempts_passed += 1
            elif word == "":
                print("You didn't even enter a word!")
            elif len(word) != len(random_word):
                print(f"The word must be {len(random_word)} letters long!")
            else:
                #g! regular check
                for i in range(len(word)):
                    letter = word[i]
                    if letter in letters:
                        letter_valid = True
                        if letter not in letters_tryed and letter not in random_word and word[i] != random_word[i]:
                            letters_tryed.append(letter)
                        if letter in random_word:
                            if letter not in some_letters:
                                some_letters.append(letter)
                            if word[i] == random_word[i]:
                                correct_letters[i] = letter
                    else:
                        letter_valid = False
                        print(f"There are no {letter} letter in english alphabet. Please try again")
                        break
                if letter_valid == True:
                    word_field[attempts_passed] = word
                    attempts_passed += 1
        else:
            break

        
    print(" ")
    print(f"There are no letters at all: {', '.join(letters_tryed)}")
    print(f"Some letters guessed: {', '.join(some_letters)}")
    print(f"Correct letters: \" {' '.join(correct_letters)} \"")
    print(f"List of all tryed words: ")
    print(f"↓" * len(word))
    for i in range(len(word_field)):
        print(f"{word_field[i]}")
    print(" ")

    #! end of the function mainLoop()

print(f"Welcome to the \"Wordle\" game!")
print(f"Wordle is a game where you need to guess a random word.")
print(f"Word will be up to 8 letters long, and you will have 10 attempts to guess the word. ( there are many words that have up to 8 letters lenght )")
print(f"Good luck\n")
continue_game = True
while continue_game != False:
    if continue_game != None:
        mainLoop()
        if game_won == False:
            print(f"You failed to guess the word \"{random_word}\" in {attempts} attempts.")
        else:
            print(f"You guessed the word \"{random_word}\" in {attempts_passed} attempts.")
    continue_game_ask = input("Would you like to play again? yes/no (y/n): ").lower()
    if continue_game_ask == "y" or continue_game_ask == "yes":
        continue_game = True
    elif continue_game_ask == "n" or continue_game_ask == "no":
        continue_game = False
    elif (continue_game_ask != "y" or continue_game_ask != "yes" ) and \
        (continue_game_ask != "n" or continue_game_ask != "no") or \
        (continue_game_ask == ""):
        continue_game = None
        print("Please enter a valid answer ( yes/no, y/n )")

print(f"\nThanks for playing! :)") #hg lol


