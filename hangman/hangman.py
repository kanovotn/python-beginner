import random
import string

def hangman():

    words = []
    with open('words.txt', 'r') as reader:
        content = reader.read()
        words = content.splitlines()

    word = random.choice(words).upper()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)


    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))

        # What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", ' '.join(word_list))

        letter = input("Guess a letter: ").upper()
        if letter in alphabet - used_letters:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)

        elif letter in used_letters:
            print("You have already used this letter. Try again.")

    print("You guessed twe word ", word, "!")

if __name__ == "__main__":
    hangman()
