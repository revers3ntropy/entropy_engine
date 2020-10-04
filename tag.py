tags = []


class Tag:
    def __init__(self, name):
        self.name = name


def find_tag(name):
    for tag in tags:
        if tag.name == str(name):
            return tag

    return False


def create_tag(name):
    if find_tag(name) is False:
        tags.append(Tag(str(name)))
