#!/usr/bin/env python3
# скрипт игры "простое ли число?"
import brain_games.games.prime as prime
from brain_games.engine import execute_game


def main():
    execute_game(prime)


if __name__ == '__main__':
    main()
