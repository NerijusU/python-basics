secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1

if guess == secret_word:
    print("You winn!")
else:
    print("You lose!")
