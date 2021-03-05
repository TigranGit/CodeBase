class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPhone(self):
        phone = Phone()

        body = self.__builder.getBody()
        phone.setBody(body)

        cpu = self.__builder.getCPU()
        phone.setCPU(cpu)

        # 3 cameras
        for _ in range(3):
            camera = self.__builder.getCamera()
            phone.attachCamera(camera)
        return phone


class Phone:
    def __init__(self):
        self.__body = None
        self.__cpu = None
        self.__cameras = list()

    def setBody(self, body):
        self.__body = body

    def attachCamera(self, camera):
        self.__cameras.append(camera)

    def setCPU(self, cpu):
        self.__cpu = cpu

    def print_specifications(self):
        print("Body color:", self.__body.color)
        print("CPU (MHz):", self.__cpu.mhz)
        print("Cameras (MP):", [camera.mp for camera in self.__cameras])


class Builder:
    def getCamera(self):
        pass

    def getCPU(self):
        pass

    def getBody(self):
        pass


class IPhoneBuilder(Builder):
    def getCamera(self):
        camera = Camera()
        camera.mp = 12
        return camera

    def getCPU(self):
        cpu = CPU()
        cpu.mhz = 2600
        return cpu

    def getBody(self):
        body = Body()
        body.color = "red"
        return body


class Camera:
    mp = None


class CPU:
    mhz = None


class Body:
    color = None


if __name__ == "__main__":
    iphone_builder = IPhoneBuilder()

    director = Director()

    print("Building an IPhone")
    director.setBuilder(iphone_builder)
    phone = director.getPhone()
    phone.print_specifications()
