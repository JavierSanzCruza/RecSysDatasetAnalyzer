class Optional:
    """
    A
    """
    def __init__(self):
        self.object = None

    @staticmethod
    def empty():
        opt = Optional()
        opt.object = None
        return opt

    @staticmethod
    def of(object):
        opt = Optional()
        opt.object = object
        return opt

    def is_empty(self):
        return self.object is None

    def get(self):
        return self.object
