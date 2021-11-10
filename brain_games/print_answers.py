# подпрограммы общения и вывода информации для различных игр
import prompt


def welcome_user_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def answer_final(name, flag):
    print('Congratulations,' if flag else "Let's try again,", name + '!')


def answer_for_input(is_correct, user_answer="", right_answer=""):
    if is_correct:
        print("Correct!")
    else:
        answer_string = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
        print(answer_string.format(user_answer, right_answer))


# def question_string(str_value):
#    print(str_value)
