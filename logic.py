import random

def start_game(MIN_NUMBER, MAX_NUMBER, ATTEMPTS, STARTING_CAPITAL):
    balance = STARTING_CAPITAL
    print(f'Вы участник игры "УГАДАЙ ЧИСЛО!". Ваш начальный капитал - {balance}')

    for attempt in range(ATTEMPTS):
        print(f'Попытка {attempt + 1}/{ATTEMPTS}')

        try:
            bet = int(input(f'Введите Вашу ставку - '))
        except ValueError:
            print('Введите корректное число для ставки.')
            continue

        if bet > balance:
            print('Ставка не может превышать имеющийся баланс!')
            continue


        guessed_number = int(input(f'Угадайте число от {MIN_NUMBER} до {MAX_NUMBER}'))
        number = random.randint(MIN_NUMBER, MAX_NUMBER)

        if guessed_number == number:
            balance += bet
            print(f'Верно! Загаданное число - {number}. Ваш обновленный баланс - {balance}')

        else:
            balance -= bet
            print(f'Неверно! Загаданным числом было - {number}. Обновленный баланс - {balance}')

        if balance <= 0:
            print('У Вас закончился баланс! Игра окончена.')
            break

    if balance > 0:
        print(f'Завершение игры! Ваш итоговый баланс - {balance}')

    else:
        print('Вы проиграли все деньги!!')