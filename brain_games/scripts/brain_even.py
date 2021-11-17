#!/usr/bin/env python3
# скрипт игры чет/нечет
from brain_games.games.game import CODE_EVEN
from brain_games.brains_engine import exec_game


def main():
    exec_game(CODE_EVEN)


if __name__ == '__main__':
    main()
