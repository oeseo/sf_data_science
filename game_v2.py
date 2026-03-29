import numpy as np # Подключи numpy.
 

def random_predict(number:int=1) -> int: # Создай функцию, которая принимает загаданное число.
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # Поставь счётчик попыток на ноль.

    while True: # Потом бесконечно:
        count += 1 # count = count + 1 увеличивай счётчик,
        predict_number = np.random.randint(1, 501) # предполагаемое число, выбирай случайное число от 1 до 100,
        if number == predict_number: # если угадал — остановись.
            break # выход из цикла, если угадали
    return(count) # После этого верни количество попыток.

print(f'Количество попыток: {random_predict()}') # Ответ. 
# result = random_predict(25)
# print(result)


def score_game(random_predict) -> int: # Возьми алгоритм угадывания и проверь, насколько он хорош
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)