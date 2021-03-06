from abc import ABCMeta, abstractstaticmethod
import copy


class Prototype(metaclass=ABCMeta):
    @abstractstaticmethod
    def clone():
        pass


class ConcreteClass1(Prototype):
    def __init__(self, number=0, string="", array=[], dictionary={}):
        self.number = number
        self.string = string
        self.array = array
        self.dictionary = dictionary

    def clone(self):
        return type(self)(
            self.number, self.string, self.array.copy(), self.dictionary.copy()
        )

    def __str__(self):
        return f"""{id(self)}
        number={self.number}
        string={self.string}
        array={self.array}
        dictionary={self.dictionary}"""


class ConcreteClass2(Prototype):
    def __init__(self, number=0, string="", array=[], dictionary={}):
        self.number = number
        self.string = string
        self.array = array
        self.dictionary = dictionary

    def clone(self):
        return type(self)(
            self.number,
            self.string,
            copy.deepcopy(self.array),
            copy.deepcopy(self.dictionary),
        )

    def __str__(self):
        return f"""number={self.number}
        string={self.string}
        array={self.array}
        dictionary={self.dictionary}
        {id(self.number)}
        {id(self.string)}
        {id(self.array)}
        {id(self.dictionary)}"""


if __name__ == "__main__":
    object1 = ConcreteClass1(1, "object1", [1, 2, 3], {"a": 4, "b": 5, "c": 6})
    print(f"object1 {object1}")
    print()

    object1_copy = object1.clone()
    object1_copy.s = "object1_copy"
    object1_copy.array[0] = 10
    print(f"object1_copy {object1_copy}")
    print(f"object1 {object1}")
    print()

    object2 = ConcreteClass2(2, "object2", [1, 2, 3], {"a": 10, "b": 5, "k": 6})
    print(f"object2 {object2}")
    print()

    object2_copy = object2.clone()
    object2_copy.s = "object2_copy"
    object2_copy.array[0] = 100
    print(f"object2_copy {object2_copy}")
    print(f"object2 {object2}")
