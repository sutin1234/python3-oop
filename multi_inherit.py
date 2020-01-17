# multi extends class


class Mom:
    def __init__(self, gender, color):
        self.gender = gender
        self.color = color

    @property
    def getPropertyOfMom(self):
        return "class: {} gender: {} color: {}".format(__class__.__name__, self.gender, self.color)


class Dad:
    def __init__(self, gender, color):
        self.gender = gender
        self.color = color

    @property
    def getPropertyOfDad(self):
        return "class: {} gender: {} color: {}".format(__class__.__name__, self.gender, self.color)


class Child(Mom, Dad):
    def __init__(self, gender, color):
        super().__init__(gender, color)

        self.gender = gender
        self.color = color

    def getChild(self):
        return "gender: {} color: {}".format(self.gender, self.color)


if __name__ == '__main__':
    m = Child('male', 'red')
    print(m.getPropertyOfMom)

    d = Child('female', 'green')
    print(d.getPropertyOfDad)
