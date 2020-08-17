import utilities
import fail_system


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
        new_point = utilities.check_vector2(point, float, 'hit_box.HitBox.check_point_collision(point)')
        if new_point is not False:

            if point[0] < self.x:
                return False

            elif point[1] > self.x + self.size_x:
                return False

            elif point[0] < self.y:
                return False

            elif point[1] > self.y + self.size_y:
                return False

            else:
                return True

        return False

    def check_hit_box_collision(self, hit_box):
        if type(hit_box) != HitBox:
            fail_system.error('hit_box passed in has to be of type HitBox. it is a ' + str(type(hit_box)), 'hit_box.check_hit_box_collision()')
        else:

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

        return False

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int, 'hit_box.HitBox.set_size(size)')
        if new_size is not False:

            self.size_x = new_size[0]
            self.size_y = new_size[1]

    def set_position(self, position):
        new_position = utilities.check_vector2(position, int, 'hit_box.HitBox.set_size(size)')
        if new_position is not False:

            self.x = new_position[0]
            self.y = new_position[1]