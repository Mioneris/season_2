from decouple import config
from logic import start_game

def main():

    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    attempts = config('ATTEMPTS' ,cast=int)
    starting_balance = config('STARTING_BALANCE', cast=int)



    start_game(min_number, max_number, attempts, starting_balance)


if __name__ == '__main__':
    main()