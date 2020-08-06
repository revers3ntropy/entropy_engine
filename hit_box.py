import utilities
import fail_system


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

    def check_point_collision(self, point):
        if utilities.check_collision(point, self.get_hit_box()):
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
