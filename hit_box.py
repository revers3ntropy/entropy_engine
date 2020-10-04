import utilities


class HitBox:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def hit_box(self):
        return self.x, self.y, self.size_x, self.size_y

    def position(self):
        return self.x, self.y

    def size(self):
        return self.size_x, self.size_y

    def check_point_collision(self, point):
        new_point = utilities.check_vector2(point, float)

        if new_point[0] < self.x:
            return False

        elif new_point[1] > self.x + self.size_x:
            return False

        elif new_point[0] < self.y:
            return False

        elif new_point[1] > self.y + self.size_y:
            return False

        return True

    def check_hit_box_collision(self, hit_box):
        hit_box = utilities.check_input(hit_box, HitBox)

        if hit_box.x + hit_box.size_x < self.x:
            return False

        elif hit_box.x > self.x + self.size_x:
            return False

        elif hit_box.y + hit_box.size_y < self.y:
            return False

        elif hit_box.y > self.y + self.size_y:
            return False

        else:
            return True

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int)

        self.size_x = new_size[0]
        self.size_y = new_size[1]

    def set_position(self, position):
        new_position = utilities.check_vector2(position, int)

        self.x = new_position[0]
        self.y = new_position[1]
