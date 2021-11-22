#!/usr/bin/env python3
# скрипт игры чет/нечет

from brain_games.engine import execute_game
import brain_games.games.even as even


def main():
    execute_game(even)


if __name__ == '__main__':
    main()
