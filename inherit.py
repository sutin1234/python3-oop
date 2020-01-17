# inheritant


class School:
    def __init__(self, name, year):
        self.name = name.upper()
        self.year = year

    def __str__(self):
        return "{}, {}, {}".format(self.__class__.__name__, self.name, self.year)

    def getSchool(self):
        return "{}, {}, {}".format(self.__class__.__name__, self.name, self.year)


class Building(School):  # extends School class
    def __init__(self, name, year):
        super().__init__(name, year)  # use init supper class to School
        self.name = name
        self.year = year

    def __str__(self):
        return "{}, {}, {}".format(self.__class__.__name__, self.name, self.year)


if __name__ == '__main__':
    b = Building("building 200 year", 2019)
    print(b.getSchool())
