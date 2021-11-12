# подпрограммы общения и вывода информации для различных игр
import prompt


def welcome_user_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name
