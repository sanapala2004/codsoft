import math
import copy

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(board, maximizing_player, alpha, beta):
    if board.current_winner == 'X':
        return -1
    elif board.current_winner == 'O':
        return 1
    elif not board.empty_squares():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in board.available_moves():
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move, 'O')
            eval = minimax(board_copy, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move, 'X')
            eval = minimax(board_copy, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(board):
    best_move = None
    best_eval = -math.inf
    for move in board.available_moves():
        board_copy = copy.deepcopy(board)
        board_copy.make_move(move, 'O')
        eval = minimax(board_copy, False, -math.inf, math.inf)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def play_game():
    t = TicTacToe()
    print("To play Tic Tac Toe, you need to input numbers as shown below:")
    TicTacToe.print_board_nums()
    print("Start the game!")
    t.print_board()
    while t.empty_squares():
        if t.num_empty_squares() % 2 == 1:
            square = int(input("Choose where to place 'X' (0-8): "))
            t.make_move(square, 'X')
        else:
            square = get_best_move(t)
            t.make_move(square, 'O')
            print(f"AI placed 'O' in square {square}")
        t.print_board()
        if t.current_winner:
            print(f"{t.current_winner} wins!")
            break
    if not t.current_winner:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
