import fail_system

tags = []


class Tag:
    def __init__(self, name):
        self.name = name


def find_tag(name):
    name = str(name)
    for tag in tags:
        if tag.name == name:
            return tag

    return False


def create_tag(name):
    name = str(name)
    if find_tag(name) is False:
        tags.append(Tag(name))
