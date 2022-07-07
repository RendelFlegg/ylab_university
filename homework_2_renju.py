import random

import numpy as np


class TicTacToe:
    """Class of game itself. Stores parameters of game and method to render board and define winner"""
    def __init__(self, length, streak):
        self.length = length
        self.streak = streak
        self.mode = 'reverse'
        self.board = {(x, y): ' ' for x in range(1, self.length + 1) for y in range(1, self.length + 1)}
        self.status = 'Game not finished'
        self.current_player = 'player_one'
        self.players = {}
        self.ai_dictionary = {}
        self.lines = get_lines(self.length, self.streak)

    def drop_board(self):
        """Return board to initial state"""
        self.board = {(x, y): ' ' for x in range(1, self.length + 1) for y in range(1, self.length + 1)}
        self.status = 'Game not finished'
        self.current_player = 'player_one'
        self.players = {}

    def show_board(self):
        """Render board"""
        print('-' * self.length * 2 + '---')
        for x in range(1, self.length + 1):
            line = []
            for y in range(1, self.length + 1):
                line.append(self.board[x, y])
            print('|', ' '.join(line), '|')
        print('-' * self.length * 2 + '---')

    def get_coordinates(self):
        """Ask human player for move"""
        while True:
            try:
                coordinates = input('Enter the coordinates: ')
                x, y = coordinates.split()
                x, y = int(x), int(y)
                assert x in range(1, self.length + 1) and y in range(1, self.length + 1)
                if self.board[x, y] != ' ':
                    print('This cell is occupied! Choose another one!')
                else:
                    return x, y
            except ValueError:
                print('You should enter numbers!')
            except AssertionError:
                print(f'Coordinates should be from 1 to {self.length}!')

    def choose_turn(self):
        return self.players[self.current_player]['mark']

    def check_mark(self, mark):
        """Check if there is filled winning line"""
        return read_lines(self.board, self.lines, self.streak, mark, 0)

    def results(self):
        for mark in ['X', 'O']:
            if self.check_mark(mark):
                if self.mode == 'classic':
                    return f'{mark} wins'
                else:
                    return f'{"O" if mark == "X" else "X"} wins'
        if ' ' in self.board.values():
            return 'Game not finished'
        else:
            return 'Draw'

    def switch_player(self):
        players_list = list(self.players.keys())
        if self.current_player == players_list[0]:
            self.current_player = players_list[1]
        else:
            self.current_player = players_list[0]

    def make_move(self):
        player_type = self.players[self.current_player]['type']
        if player_type == 'user':
            return self.get_coordinates()
        else:
            return self.ai_dictionary[player_type].ai_move()

    def game(self):
        """Game engine"""
        self.show_board()
        while self.status == 'Game not finished':
            self.board[self.make_move()] = self.choose_turn()
            self.switch_player()
            self.status = self.results()
            self.show_board()
        print(self.status)
        self.drop_board()

    def get_command(self):
        print('Available players with current game parameters:\n'
              '"user" - Human player, mostly harmless\n'
              '"easy" - Basic AI player, moves randomly\n'
              '"medium" - Advanced AI player,'
              ' in Classic streak defends himself at critical moments and attacks when feels blood.'
              ' In Reverse streak tries not to loose accidentally')
        if self.length == self.streak == 3 and self.mode == 'classic':
            print('"hard" - Supreme AI player, Undefeated Champion. Test your might!')
        while True:
            print('\nType a command in following order:\n'
                  '"start %%PLAYER_ONE%% %%PLAYER_TWO%%"\n'
                  'Player one plays with "X". For exit type "exit"\n')
            try:
                raw_input = input('Input command: ')
                if raw_input == 'exit':
                    return raw_input
                command, player_one, player_two = raw_input.split()
                assert command == 'start' and 'user' in (player_one, player_two) and player_one != player_two
                self.players = {'player_one': {'type': player_one, 'mark': 'X'},
                                'player_two': {'type': player_two, 'mark': 'O'}}
                return command
            except (AssertionError, ValueError):
                print('Bad parameters!')

    def get_parameters(self):
        user_input = None
        while user_input not in ("default", "customize"):
            print('Do you prefer to play with default parameters (board size - 10x10, streak - 5, mode - reversed)?')
            print('Type "default" or "customize"')
            user_input = input()
        if user_input == 'default':
            self.length = 10
            self.streak = 5
            self.mode = 'reverse'
        else:
            length = streak = mode = ''
            while not length.isdigit():
                length = input('Enter board length:\n')
            while not streak.isdigit():
                streak = input('Enter streak:\n')
            while mode not in ("classic", "reverse"):
                mode = input('Choose game streak: "classic" or "reverse"\n')
            self.length = int(length)
            self.streak = int(streak)
            self.mode = mode
        self.lines = get_lines(self.length, self.streak)
        self.board = {(x, y): ' ' for x in range(1, self.length + 1) for y in range(1, self.length + 1)}
        print(len(self.lines))

    def menu(self):
        print('Welcome to Tic Tac Toe 2000')
        self.get_parameters()
        command = self.get_command()
        while command != 'exit':
            self.game()
            user_input = None
            while user_input not in ('y', 'n'):
                user_input = input('Do you like to change parameters? y/n?\n')
            if user_input == 'y':
                self.get_parameters()
            command = self.get_command()


class AiBasic:
    """Basic class of AI player. Moves randomly."""
    def __init__(self, game_object):
        self.game_object = game_object

    def get_moves(self, v_board=None):
        board = self.game_object.board
        if v_board:
            board = v_board
        return [key for key in board if board[key] == ' ']

    def random_move(self):
        move_list = self.get_moves()
        return random.choice(move_list)

    def ai_move(self):
        print('Making move level "easy"')
        return self.random_move()


class AiAdvanced(AiBasic):
    """Advanced AI player. Can defend and attack in Classic streak. In Reverse streak tries not to lose accidentally."""
    def __init__(self, game_object):
        super().__init__(game_object)
        self.mark = None
        self.opponent_mark = None

    def update_marks(self):
        self.mark = self.game_object.players[self.game_object.current_player]['mark']
        self.opponent_mark = 'O' if self.mark == 'X' else 'X'

    def defend(self):
        """If opponent can get a win on the next move - block him"""
        return read_lines(self.game_object.board, self.game_object.lines, self.game_object.streak - 1,
                          self.opponent_mark, 0, to_win=False)

    def attack(self):
        """If AI can get a win on the next move - DO IT!"""
        return read_lines(self.game_object.board, self.game_object.lines, self.game_object.streak - 1,
                          self.mark, 0, to_win=False)

    def random_move_reverse(self, move_list):
        """Alternative random move for Reverse streak"""
        idx = random.randint(0, len(move_list) - 1)
        move = move_list.pop(idx)
        if len(move_list) == 0:
            return move
        new_board = self.game_object.board.copy()
        new_board[move] = self.mark
        if read_lines(new_board, self.game_object.lines, self.game_object.streak, self.mark, 0):
            return self.random_move_reverse(move_list)
        return move

    def ai_move(self):
        self.update_marks()
        print('Making move level "medium"')
        if self.game_object.mode == 'classic':
            return self.defend() or self.attack() or self.random_move()
        else:
            move_list = self.get_moves()
            return self.random_move_reverse(move_list)


class AiSupreme(AiAdvanced):
    """Undefeated champion. Currently available only on 3x3 board in Classic streak"""
    def ai_move(self):
        self.update_marks()
        print('Making move level "hard"')
        if len(self.get_moves()) == self.game_object.streak ** 2:
            return 1, 1
        return self.best_move(self.game_object.board)

    def best_move(self, new_board):
        """Return best move with Minimax algorithm"""
        best_score = -10000
        best_move = None
        move_list = self.get_moves(v_board=new_board)

        for move in move_list:
            new_board[move] = self.mark
            score = self.minimax(new_board, 0, False)
            new_board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, new_board, depth, is_maximising):
        move_list = self.get_moves(v_board=new_board)
        if read_lines(new_board, self.game_object.lines, self.game_object.streak, self.opponent_mark, 0):
            return -1
        elif read_lines(new_board, self.game_object.lines, self.game_object.streak, self.mark, 0):
            return 1
        elif len(move_list) == 0:
            return 0

        if is_maximising:
            best_score = -10000
            for move in move_list:
                new_board[move] = self.mark
                score = self.minimax(new_board, depth + 1, False)
                new_board[move] = ' '
                if score > best_score:
                    best_score = score
            return best_score

        else:
            best_score = 10000
            for move in move_list:
                new_board[move] = self.opponent_mark
                score = self.minimax(new_board, depth + 1, True)
                new_board[move] = ' '
                if score < best_score:
                    best_score = score
            return best_score


def process_line(line, length):
    """Slices list of coordinates to smaller ones"""
    line_list = []
    for n in range(len(line) - length + 1):
        line_list.append(list(line)[n:n + length])
    return line_list


def get_lines(size, streak):
    """Return all possible lines, that can be taken for a win"""
    difference = size - streak
    lines_list = []
    list_of_rows = []
    for x in range(1, size + 1):
        row = [(x, y) for y in range(1, size + 1)]
        list_of_rows.append(row)
    matrix = np.array(list_of_rows, dtype='i,i')  # Create coordinates matrix
    for row in matrix:
        lines_list += process_line(row, streak)
    for column in matrix.T:
        lines_list += process_line(column, streak)
    for n in range(-difference, difference + 1):
        diagonal = np.diag(matrix, k=n)  # Get all possible diagonals from left to right
        reverse_diagonal = np.diag(np.fliplr(matrix), k=n)  # And diagonals from right to left
        lines_list += process_line(diagonal, streak)
        lines_list += process_line(reverse_diagonal, streak)
    return lines_list


def read_lines(board, lines, limit, mark, idx, to_win=True):
    """Function helps the Game an AI read current position on board"""
    counter = 0
    move = None
    for coord in lines[idx]:
        coord = tuple(coord)  # Handling numpy.void type
        if board[coord] == mark:
            counter += 1
        if board[coord] == ' ':
            move = coord
    if counter == limit:
        if to_win:
            return True
        elif move:
            return move
        else:
            return read_lines(board, lines, limit, mark, idx + 1, to_win=to_win)
    else:
        if idx == len(lines) - 1:
            return None
        return read_lines(board, lines, limit, mark, idx + 1, to_win=to_win)


if __name__ == '__main__':
    tic_tac_toe = TicTacToe(10, 5)
    alpha = AiBasic(tic_tac_toe)
    beta = AiAdvanced(tic_tac_toe)
    gamma = AiSupreme(tic_tac_toe)
    tic_tac_toe.ai_dictionary['easy'] = alpha
    tic_tac_toe.ai_dictionary['medium'] = beta
    tic_tac_toe.ai_dictionary['hard'] = gamma
    tic_tac_toe.menu()
