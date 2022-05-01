# Guessing the Number Game (Text-version)  (Easy One)
# This guessing game only supports for number from 1 to 100.
import random
from datetime import datetime
from stack import Stack

s = Stack()  # Stack Initialization


def confirm_current_stack() -> None:
    print(s.items)


def random_number_generator() -> int:
    return_num = random.randint(1, 100)
    return return_num


def get_user_input() -> str:
    while True:
        try:
            number = input("First, please select your favorite number from 1 to 100: ")
            break
        except ValueError:
            print("Please do not type in blank space or some other type of things")
    if len(number) == 0:  # Checks character (Avoid the cause of error)
        print("This is not acceptable input. Please try number")
        get_user_input()
    if int(number) < 1 or int(number) > 100:
        print("Please select number from designated range.")
        get_user_input()
    return number


def ask_for_replay() -> None:
    selection = input("Do you want to try it again? Y/N/y/n:  ")
    # Asks for replay until user types n or N in the console.
    while selection in "Yy":
        main()
        selection = input("Do you want to try it again? Y/N/y/n:  ")
    return None


def write_to_txt_file() -> None:
    # Open txt file as append mode (write will delete existing contents)
    # and add the current steps taken and time when completion.
    with open('ranking.txt', 'a') as f:
        for item in s.items.pop():
            f.write(str(item))
            f.write(str(","))
        # f.write(str(s.items.pop()))
        f.write("\n")


def read_ranking_txt() -> None:
    """
    This function returns Nothing but read the text file which is "ranking.txt"
    """
    with open("ranking.txt", "r") as f:
        print(f.read())


def main() -> None:
    r_num = random_number_generator()
    print(r_num)
    number = 0  # initial state
    counter = 0
    while r_num != number:
        number = int(get_user_input())
        if number < r_num:
            print("Your selected number is lower than what computer selects  ")
        else:
            print("Your selected number is higher than computer selection")
        counter += 1
    print("Wow, You did it!!!!!!")
    print("You took %d times for this guessing game" % counter)
    print("We will save your result in the stack for this game.")
    # [steps, random number selected, date and time]
    name = input("Please type in your name here (nickname is acceptable):  ")
    s.push([name, counter, r_num, datetime.today().strftime('%Y-%m-%d')])
    write_to_txt_file()
    confirm_current_stack()


if __name__ == "__main__":
    print("This is the start of the Number Guessing Game!!!")
    main()
    ask_for_replay()
    read_ranking_txt()
