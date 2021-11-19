from random import randint

# максимальное число в игре
PRIME_RANGE = 50
QST_STR = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    i = 2
    limit = int(n ** 0.5)
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def main():
    """Игра 'Правильное ли число?'
    функция генерирует случайное число от 0 до PRIME_RANGE - 1
    для определения простоты числа используется список prime_array
    возвращает два параметра - ответ игрока и правильный ответ"""

    random_number = randint(0, PRIME_RANGE - 1)
    right_answer = "yes" if is_prime(random_number) else "no"
    return random_number, right_answer
