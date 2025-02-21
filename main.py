my_lucky_number = 7
while True:
    try:
        guess = int(input("Guess my lucky number! I think it is: "))
        if guess == my_lucky_number:
            print("Congrats! You guessed it.")
            break
    except ValueError:
        print("Please enter a valid number!")
