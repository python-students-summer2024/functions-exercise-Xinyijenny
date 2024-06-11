"""
An education app that elementary school teachers can use to help teach their students learn addition and subtraction. 
The app allows students to virtually roll two dice. The values of the dice will be displayed to the students, and the app will then ask students to input either the sum of the two dice or the difference between the two dice. 
Students are told whether their answer was correct or not.
"""

from app_functions import * 


def main():
    """
    Use the functions defined in app_functions.py to make this game work.

    The flow of the game goes as follows:
    - Rolls two virtual dice to generate two pseudo-random numbers between 1 and 6, inclusive.
    - Pseudo-randomly decide whether the question will be an addition or a subtraction question.
    - Present the question to the user and ask them to enter their response.
    - If the user entered an invalid response, print an error message and do nothing further (i.e. do not do the next two steps below).
    - If their answer was correct, congratulate them.
    - If their answer was incorrect, show them the correct answer.
    """
    print("")  # line break
    print("Welcome to the Math App!!!")
    print("")  # line break
    ### write code to complete this function BELOW here ###
    die_1 = roll_die()
    die_2 = roll_die()
    question_type = get_question_type()
    print_question(die_1, die_2, question_type)
    answer = input_answer()
    if answer == -1:
        print_error_message()
    if is_correct_answer(die_1 ,die_2, question_type, answer) is True:
        print_congratulations(question_type)
    elif is_correct_answer(die_1 ,die_2, question_type, answer) is False:
        print_correct_answer(die_1, die_2, question_type)
    



    ### write code to complete this function ABOVE here ###
    print("")  # line break
    print("Game over!!!")
    print("Thank you for playing!!!\n")


# call the main function
main()
