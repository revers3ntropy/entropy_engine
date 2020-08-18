class BoardController:
    def __init__(self, squares, sq_size):
        self.board = self.gen_board(8, 8)
        self.squares = squares
        self.square_size = sq_size

    def gen_board(self, width, height):
        grid = []
        for j in range(width):
            line = []
            for k in range(height):
                line.append(None)
            grid.append(line)
        return grid

    def move_piece(self, original_square, new_square):
        if self.board[new_square[0]][new_square[1]] is not None:
            pass
        else:
            piece = self.board[original_square[0]][original_square[1]]
            self.board[original_square[0]][original_square[1]] = None

            self.board[new_square[0]][new_square[1]] = piece

            self.update_peices()

    def set_piece(self, piece, position):
        self.board[position[0]][position[1]] = piece

    def chack_legal_state(self):
        return True

    def update_peices(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    piece = self.board[i][j]
                    piece.get_component('body').go_to((i * self.square_size, j * self.square_size))

    def update(self):
        self.update_peices()
