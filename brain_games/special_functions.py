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


def generate_prime_list(depth=100):
    """генерируется список в диапозоне 0 - (depth-1),
    тип bool. Проверка 'простоты' числа осуществляется с
    помощью индекса, равного этому числу"""
    # алгоритм строится на основе 'Решета Эратосфена'
    prime_list = [True] * depth
    prime_list[0] = prime_list[1] = False  # 0,1 - не простые
    for count in range(2, depth):
        if prime_list[count]:
            # меняется на False все, что кратное текущему
            # простому числу и двум
            for n in range(2 * count, depth, count):
                prime_list[n] = False
    return prime_list
