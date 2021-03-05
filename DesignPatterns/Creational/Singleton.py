class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # To run __init__ every time the class is called
        # else:
        #     cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class SomeSingletonClass(metaclass=Singleton):
    value = 0

    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    myClass = SomeSingletonClass(500)
    print(myClass.value)
    otherClass = SomeSingletonClass(700)
    print(otherClass.value)
