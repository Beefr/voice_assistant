

class SessionManagerMeta(type):

    _instances = {}


    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class SessionManager(metaclass=SessionManagerMeta):

    def __init__(self):
        pass

    def newSession(self, username):
        pass