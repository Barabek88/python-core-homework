class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        return self.name == 'Rock' and other.name == 'Scissors' or \
               self.name == 'Paper' and other.name == 'Rock' or \
               self.name == 'Scissors' and other.name == 'Paper'

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
