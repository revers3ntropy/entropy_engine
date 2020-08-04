def add_vectors(v1, v2):
    v3 = [v1[0] + v2[0], v1[1] + v2[1]]
    return v3


def check_collision(point, hit_box):
    if hit_box[0] < point[0] < hit_box[0] + hit_box[2] and hit_box[1] < point[1] < hit_box[1] + hit_box[3]:
        return True
    return False
