import random

from random_word import RandomWords


def adamak(guesses, wd):
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif guesses == 6:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n")
        print("The word was %s." % wd)
        print("\n")
        print("\n game over LOSER")


def selectWord():
    r = RandomWords()
    myword = r.get_random_word(hasDictionaryDef=True)

    return myword


def hangMan():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman!\n")
    adamak(guesses, word)
    print("\n")
    print("" + " ".join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < 6:

        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print("you should enter one letter each time!not anymore!")
        elif guess == "":
            print("dude you should enter a letter")
        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(" ".join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                adamak(guesses, word)

                if guesses < 6:
                    print("Guess again.")
                    print(" ".join(blanks_list))

            elif word_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(" ".join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WoN!")
                else:
                    print("Great guess! Guess another!")


hangMan()
