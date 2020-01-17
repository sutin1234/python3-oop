class Walet:
    def __init__(self):
        self.amount = 0

    def earn(self, a):
        self.amount = a

    def spen(self, a):
        self.amount -= a

    def __str__(self):
        return (" amount = {}".format(self.amount))

    @property  # made properties with function
    def getAmonut(self):
        return ("amount = {}".format(self.amount))


if __name__ == '__main__':
    w = Walet()
    w.earn(100)
    print("dad's wallet {}".format(w))

    m = w
    print("mom's wallet {}".format(m))

    m.spen(30)
    print("dad's wallet {}".format(m))
    print("mom's wallet {}".format(m))
    print(id(w), id(m))

    print(w.getAmonut)
