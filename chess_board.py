class BoardController:
    def __init__(self, squares):
        self.board = self.gen_board(8, 8)
        self.squares = squares

    def gen_board(self, width, height):
        grid = []
        for j in range(width):
            line = []
            for k in range(height):
                line.append(None)
            grid.append(line)
        return grid

    def move_piece(self, original_square, new_square):
        piece = self.board[original_square[0]][original_square[1]]
        self.board[original_square[0]][original_square[1]] = None

        self.board[new_square[0]][new_square[1]] = piece

    def set_piece(self, piece, position):
        self.board[position[0]][position[1]] = piece
