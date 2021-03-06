class Shirt:
    title = None
    color = None

    def setTitle(self, title):
        self.title = title

    def setColor(self, color):
        self.color = color

    def getTitle(self):
        return self.title

    def getColor(self):
        return self.color

    def calculatePrice(self):
        return len(self.title) * len(self.color)

    def printSpecifications(self):
        print("Shirt title:", self.title)
        print("Shirt color:", self.color)
        print("Shirt price:", self.calculatePrice())


class NikeShirt(Shirt):
    title = "Nike"

    def __init__(self):
        super().__init__()

    def calculatePrice(self):
        return super().calculatePrice() * 10


class AdidasShirt(Shirt):
    title = "Adidas"

    def __init__(self):
        super().__init__()

    def calculatePrice(self):
        return super().calculatePrice() * 8


class EcoShirt(Shirt):
    title = "Eco (100% cotton)"

    def __init__(self):
        super().__init__()

    def calculatePrice(self):
        return super().calculatePrice() * 5


class ShirtFactory:
    def getShirt(self, shirtName):
        if "nike" in shirtName.lower():
            return NikeShirt()
        elif "adidas" in shirtName.lower():
            return AdidasShirt()
        elif "eco" in shirtName.lower():
            return EcoShirt()
        else:
            print("Warning: Unecpected Shirt name", shirtName)
            shirt = Shirt()
            shirt.setTitle(shirtName)
            return shirt


if __name__ == "__main__":
    factory = ShirtFactory()

    shirtName = input("Enter shirt name: ")
    shirtColor = input("Enter shirt color: ")

    shirt = factory.getShirt(shirtName)
    shirt.setColor(shirtColor)

    shirt.printSpecifications()
