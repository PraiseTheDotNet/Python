from lab8.task1.Entity import Entity


class Artist (Entity):
    name = ''

    def __init__(self, name):
        super().__init__()
        self.name = name
