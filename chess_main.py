import entropy_engine as ee
import chess_pieces
from chess_board import BoardController

ee.init((1000, 600))

board = ee.create_sprite('board')
board_controller = board.add_component('script')
board_body = board.add_component('body')

square_size = 50
squares = []
board_offset = (500, 400)

for i in range(8):
    for j in range(8):
        # create square
        sq = ee.create_sprite(f'sq {i},{j}')

        sq_body = sq.add_component('body')
        sq_body.go_to((i * square_size, j * square_size))

        square = sq.add_component('rect renderer')
        square.set_size((square_size, square_size))

        if (i + j) % 2 == 0:
            colour = (200, 200, 200)  # light squares
        else:
            colour = (15, 15, 15)  # dark squares
            print(colour)
        square.set_colour(colour)

        squares.append(sq)

board_controller.set_script(BoardController(squares))

# moving the camera
ee.find_sprite('camera').get_component('body').go_to(board_offset)


def new_piece(name_, type_, board_coords_, image_, colour_):
    sprite = ee.create_sprite(name_)

    sprite.add_component('body')

    image = sprite.add_component('image')
    image.set_image_from_file(image_)

    sprite.add_component('script').set_script(chess_pieces.PieceController(sprite, board, colour_, type_))

    board_controller.script.set_piece(sprite, board_coords_)


for i in range(8):
    new_piece(f'{i} white pawn', chess_pieces.pawn, (i, 2), 'graphics/chaos_14x16/0.png', chess_pieces.white)
    new_piece(f'{i} black pawn', chess_pieces.pawn, (i, 7), 'graphics/chaos_14x16/0.png', chess_pieces.black)


ee.run_game()
