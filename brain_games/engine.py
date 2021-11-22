import prompt


ROUND_COUNT = 3        # количество циклов в игре


def execute_game(game):
    """ входные параметры - имя игры, имя игрока"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name + '!')
    print(game.RULES)   # возвращается только строка с правилами
    is_winner = True
    count = ROUND_COUNT
    while count > 0 and is_winner:
        task, correct_answer = game.get_question_and_answer()
        answer = prompt.string("Question: {0}\nYour answer: ".format(task))
        if answer == correct_answer:
            count -= 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            is_winner = False
    print("Congratulations," if is_winner else "Let's try again,",
          user_name + "!")
