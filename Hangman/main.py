# Ask player 1 for a word
print('Speler 1, typ het te raden woord:')
word = input("Typ het te raden woord: ").lower()

guessed = False
guessed_letters_count = 0
wrong_guesses = 0
word_array = ["_" for _ in word]

# Keep game going if not guessed
while not guessed:
    print("Status van het woord:", " ".join(word_array))
    letter = input("Raad een letter: ").lower()

    # If the currently guessed letter is in the word, check what position it is in. Then increase the amount of guessd letters.
    if letter in word:
        for index, char in enumerate(word):
            if char == letter and word_array[index] == "_":
                word_array[index] = letter
                guessed_letters_count += 1
                
    # Else increase the wrong guesses and print the wrong guess text
    else:
        wrong_guesses += 1
        print(f"Foute gok, je hebt nu {wrong_guesses} fout(en). Je mag maximaal 8 fouten maken.")
    
    # If the length of word is the same as the guessed letter count print the 'you've won' text
    if guessed_letters_count == len(word):
        print(f"Yess!! Je hebt gewonnen! Het woord was '{word}'.")
        guessed = True

    # If the wrong guesses is equal or greater then 8 (limited amount of guesses), print the 'you've lost' text
    if wrong_guesses >= 8:
        print(f"Helaas, game over! Je hebt te veel letters geprobeerd. Het woord was: '{word}'.")
        guessed = True
