class HitBox:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def get_hit_box(self):
        return self.x, self.y, self.size_x, self.size_y

    def position(self):
        return self.x, self.y

    def size(self):
        return self.size_x, self.size_y

    def x(self):
        return self.x

    def gy(self):
        return self.x

    def size_x(self):
        return self.size_x

    def size_y(self):
        return self.size_y()


    def check_point_collision(self, point):
        if self.x[0] < point[0] < self.x + self.size_x and self.y < point[1] < self.y + self.size_y:
            return True
        return False

    def check_hit_box_collision(self, hit_box):
        return False
