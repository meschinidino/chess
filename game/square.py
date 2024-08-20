class Square:
    def __init__(self, color):
        self.color = color
        self.piece = None

    def get_color(self):
        return self.color

    def set_piece(self, piece):
        self.piece = piece

    def has_piece(self):
        return self.piece is not None