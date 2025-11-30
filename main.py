import random
import hangman_art

stages = hangman_art.stages

words = ["Bicycle", "Mountain", "Jungle", "Galaxy", "Whistle"]
word = random.choice(words)

print(stages[6])

blanks = "_" * len(word)
print(blanks, "\n") 

lives = 6
guessed_letters = []
correct_letters = []
game_over = False

print("lives: 6\n")
while not game_over:

# Ask user for guess
    guess = input("Enter your guess: ").lower().strip()

# Check if guess is single alphabet
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input")
        continue
    if guess in guessed_letters:
        print("Already guessed.")
        continue
    else:
        guessed_letters.append(guess)

# Display the updated word to user
    display = ""
    
    for letter in word.lower():
        if guess == letter:
            display += guess
            correct_letters.append(guess)
            print(f"'{guess}' is in word.")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

# If guess is not in word decuct a live
    if guess not in word.lower():
        lives -= 1
        print("\nIncorrect guess, Try Again!")
        print(f"lives left: {lives}")

# Print Stage of Hangman
    if lives >= 0 and lives < len(stages):
        print(stages[lives])

    print("word: ", display, "\n")

# If user has no lives left End Game
    if lives < 1:
        print("You have exhausted all your lives.")
        print("************ GAME OVER ************\n")
        game_over = True

# If user guessed all word End Game
    if "_" not in display:
        print("🎉 Congratulations! You guessed all the letters!\n")
        game_over = True

# Reveal the word once game Ends.
print(f"Word was '{word}'")
print("Thanks for playing! See you next time 👋")