pawn = 0
knight = 1
bishop = 2
rook = 3
queen = 4
king = 5

white = 0
black = 1


class PieceController:
    def __init__(self, type_, sprite, board, colour):
        self.__type_ = type_
        self.__sprite = sprite
        self.__being_moved = False
        self.moved = False
        self.__board_sprite = board
        self.__board_controller = None
        self.colour = colour
        self.__body = None

    def start(self):
        self.__board_controller = self.__board_sprite.get_component('script')[0]
        self.__body = self.__sprite.get_component('body')

    def check_move(self, new_position):
        if self.__board_controller.check_legal_state():
            return True
        return False


class PawnController(PieceController):
    def __init__(self, type_, sprite, board, colour):
        super().__init__(type_, sprite, board, colour)

    def move(self, board, new_position):
        # checks if you are trying to take or not
        if self.__board_controller.board[new_position[0]][new_position[1]] is None:
            pass
            # moving to a empty square
        else:
            pass
            # taking
