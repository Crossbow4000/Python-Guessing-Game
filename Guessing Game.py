gameHasStarted = False
wantsToContinue = True
guessedNumberIsInt = True
numberHasBeenGuessed = False

randomNumber = random.randint(0, 1000)

input("Welcome to the Number Guessing Game, press ENTER to start the game   ")

while wantsToContinue == True:
    
    guessedNumber = input("Guess a number between 0 and 1000   ")
    
    try:
        guessedNumberInt = int(guessedNumber)
    except:
        guessedNumberIsInt = False
        while guessedNumberIsInt == False:
            try:
                guessedNumberInt = int(guessedNumber)
            except:
                guessedNumber = input("That's not a number, try again   ")
            else:
                guessedNumberIsInt = True
                break
            
    while numberHasBeenGuessed != randomNumber:
        if guessedNumberInt < randomNumber:
            guessedNumber = input("That number was too low, try guessing a higher number   ")
            try:
                guessedNumberInt = int(guessedNumber)
            except:
                guessedNumberIsInt = False
                while guessedNumberIsInt == False:
                    try:
                        guessedNumberInt = int(guessedNumber)
                    except:
                        guessedNumber = input("That's not a number, try again   ")
                    else:
                        guessedNumberIsInt = True
                        break
        elif guessedNumberInt > randomNumber:
            guessedNumber = input("That number was too high, try guessing a lower number   ")
            try:
                guessedNumberInt = int(guessedNumber)
            except:
                guessedNumberIsInt = False
                while guessedNumberIsInt == False:
                    try:
                        guessedNumberInt = int(guessedNumber)
                    except:
                        guessedNumber = input("That's not a number, try again   ")
                    else:
                        guessedNumberIsInt = True
                        break
        elif guessedNumberInt == randomNumber:
            quit = input("Wow you guessed the number! Type QUIT to quit or press ENTER to play again   ")
            
            if quit.lower == "quit":
                wantsToContinue = False
                break
            else:
                wantsToContinue = True
                randomNumber = random.randint(0, 1000)
                break
