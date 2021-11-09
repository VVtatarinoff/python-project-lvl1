# способо Евклида - через последовательное деление
# Алгоритм: если большее из вдух чисел делится на меньшее -
# наименьшее и будет их НОД
# другими словами
# 1 Большее поделить на меньшее
# 2 Меньшее число поделить на остаток, который получается
#    после деления
# 3 Первый остаток поделить на второй остаток
# 4 Деление прододжается до тех пор, пока в остатке
#    не получится 0. Последний делитель и есть НОД

def find_gcd(input1, input2):
    # сортируем по возрастанию
    if input1 > input2:
        min_value = input2
        max_value = input1
    else:
        min_value = input1
        max_value = input2
    while max_value % min_value != 0:
        # предыдущее меньшее число становится большим
        # остаток становится текущим меньшим числом
        max_value, min_value = min_value, max_value % min_value
    return min_value


# ответ "yes" - если четное, иначе - "no"
def answer_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"
