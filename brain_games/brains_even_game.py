import prompt
from random import randint


def welcome_user_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def answer_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def is_winner():
    attempt_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while attempt_count > 0:
        random_number = randint(1, 100)
        answer_string = 'Question: ' + str(random_number) + '\nYour answer: '
        answer = prompt.string(answer_string)
        correct_answer = answer_even(random_number)
        if answer == correct_answer:
            attempt_count -= 1
            print('Correct!')
        else:
            answer_string = "'" + answer + "' is wrong answer ;(. "
            answer_string += "Correct answer was '" + correct_answer + "'"
            print(answer_string)
            return False
    return True


def play_even_game():
    user_name = welcome_user_new()
    if is_winner():
        print('Congratulations, ' + user_name + '!')
    else:
        print("Let's try again, " + user_name + '!')
