import math
import os
import random

class GuessNumber:

    def __init__(self) -> None:
        """Initializing variables used in below program"""
        self.lower = None
        self.higher = None
        self.chances = None
        self.number = None


    def clear_terminal(self):
        """Method to clear the terminal screen"""
         # for windows 'nt' - 'cls' for other os 'clear'
        return os.system('cls' if os.name == 'nt' else 'clear')
    

    def user_input(self):
        """Method to get user input"""
        while True:
            try:
                # get the lower and higher bound
                self.lower = int(input("Enter lower limit: "))
                self.higher = int(input("Enter higher limit: "))

                if self.lower >= self.higher:
                    # checks if lower number is greater than higher and continue if True
                    print("\nError in entering the range, higher limit should be greater than lower limit.\n")
                    continue
                return
            
            except ValueError:
                # if type of values entered by user is other than int
                print("Enter integer values only.\n")


    def generate_random_number(self):
        """Method generates random number using random.randint()"""
        self.number = random.randint(self.lower, self.higher)


    def play_game(self):
        """Method to play game to check if guessed number is correct"""
        # to get number of chances
        self.chances = math.ceil(math.log(self.higher - self.lower + 1, 2))

        # to store the guessed numbers
        guessed_number = []

        # initialze winning if the 
        winning = False

        # guess numbers until until you win or you run out of chances
        while self.chances > 0:
            # get the guess of user
            guess = self.get_guess()

            # check if number if equal or not
            if guess == self.number:
                print(f"\nYou guessed the number {self.number} right, you WON!")
                winning = True
                break

            elif guess < self.number:
                print("\nYou guessed 'LOWER'")

            else:
                print("\nYou guessed 'HIGHER'")

            guessed_number.append(guess)

            print("Your guesses:", guessed_number)
            self.chances -= 1
            
        
        # print the player lost and print the number
        if not winning:
            print(f"\nYou ran out of chances, you LOST! \nThe number was {self.number}")


    def get_guess(self):
        """Method to get the guess"""
        while True:
            try:
                # user input for guess
                self.guess = int(input(f"\nYou have {self.chances} chances\nGuess a number: "))

                # if user guess is out of bound then take input again
                if self.guess < self.lower or self.guess > self.higher:
                    print(f"Enter number i.e in range of {self.lower} and {self.higher}.\n")
                    continue
                # if guess is in bound then return guess
                return self.guess
            
            except ValueError:
                # if any other datatype is entered raise an error
                print("Enter integer value only.\n")


    def want_play_again(self):
        """Method to check if the user wants to play again"""
        # returns True for user input 'y' or "Y" or 'YES' or 'yes'
        return input("\nDo you want to play again (Y/N)? ").strip().upper().startswith('Y')
    

    def run(self):
        """Main method to run the program"""
        # the loop will run infinitely until user says 'no'
        while True:
            self.clear_terminal()
            self.user_input()
            self.generate_random_number()
            self.play_game()
            
            # if user dont want to play again exit
            if not self.want_play_again():
                print("\nThank You for playing")
                break

if __name__ == '__main__':
    # creating instance to the class GuessNumber
    g1 = GuessNumber()
    # call the main run() method
    g1.run()