import random
import hangman_words
import hangman_art

#update wordlist from hangman_words.py
word_list = hangman_words.word_list

#update stages from hangman_art.py
stages = hangman_art.stages

#Display the logo
logo = hangman_art.logo
print(logo
      )
#choose a random word from wordlist
chosen_word= random.choice(word_list)
print(chosen_word)

#To display blanks
display_word = ""
for letter in chosen_word:
    display_word += "_"
print(display_word)

guessed_letters_list = []
correct_guessed_letters_list = []
lives = 6
game_over = False

#Main Program
while not game_over:
    print(f"***YOU HAVE {lives} LIVES LEFT***")
    guessed_letter = input("Guess any letter: \n").lower()

#To alert the user about repetition
    if guessed_letter in guessed_letters_list:
        print(f"You have already guessed the letter   {guessed_letter}   !  Try another letter")
    else:
        guessed_letters_list.append(guessed_letter)
        display_word = ""
        for letter in chosen_word:
            if letter == guessed_letter:
                display_word += guessed_letter
                correct_guessed_letters_list.append(guessed_letter)
            elif letter in correct_guessed_letters_list:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

#If letter guessed is not in the word
        if guessed_letter not in chosen_word:
            lives -= 1
            print(f"The letter {guessed_letter} is not in the word\nYou lost a life!")
            if lives == 0:
                print("Game Over!!\tYou lose!!!\nThe correct word was " + chosen_word)
                game_over = True

#To complete the hangman drawing
        print(stages[lives])

#If the user successfully guessed the word
        if "_" not in display_word:
            game_over = True
            print("Yay! You Guessed Correctly!! You won!!!")

