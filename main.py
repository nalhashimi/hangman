import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
print(hangman_art.logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
lives = 6

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = list(placeholder)

    if guess in display:
        print(f"You've already guessed {guess}")
    i = 0
    guessed_right = False
    for letter in chosen_word:
        if letter == guess:
            display[i] = letter
            guessed_right = True
        i += 1
    placeholder = ''.join(display)

    if not guessed_right:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    game_over = chosen_word == placeholder or lives == 0
    print(hangman_art.stages[lives])
    print(placeholder)
    if chosen_word == placeholder:
        print("You win!")
    if lives == 0:
        print(f"IT WAS {chosen_word}! YOU LOSE!")