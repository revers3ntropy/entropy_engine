import utilities


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

    def y(self):
        return self.x

    def size_x(self):
        return self.size_x

    def size_y(self):
        return self.size_y()

    def check_point_collision(self, point):
        if utilities.check_collision(point, self.get_hit_box()):
            return True
        return False

    def check_hit_box_collision(self, hit_box):
        if self.check_point_collision((hit_box.x(), hit_box.y())):
            return True
        if self.check_point_collision((hit_box.x() + hit_box.size_x(), hit_box.y())):
            return True
        if self.check_point_collision((hit_box.x(), hit_box.y() + hit_box.size_y())):
            return True
        if self.check_point_collision((hit_box.x() + hit_box.size_x(), hit_box.y() + hit_box.size_y())):
            return True

        if utilities.check_collision((self.x(), self.y()), hit_box):
            return True
        if utilities.check_collision((self.x() + self.size_x(), self.y()), hit_box):
            return True
        if utilities.check_collision((self.x(), self.y() + self.size_y()), hit_box):
            return True
        if utilities.check_collision((self.x() + self.size_x(), self.y() + self.size_y()), hit_box):
            return True
        return False
