#!/usr/bin/env python3
# скрипт игры чет/нечет

from brain_games.brains_engine import exec_game
import brain_games.games.brains_even_game


def main():
    exec_game(brain_games.games.brains_even_game)


if __name__ == '__main__':
    main()
