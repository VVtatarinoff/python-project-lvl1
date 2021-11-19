#!/usr/bin/env python3
# скрипт игры "простое ли число?"
import brain_games.games.brains_prime_game
from brain_games.brains_engine import exec_game


def main():
    exec_game(brain_games.games.brains_prime_game)


if __name__ == '__main__':
    main()
