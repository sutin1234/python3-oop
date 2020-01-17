class Studen:
    def __init__(self, sid, fname, lname, blood):
        self.sid = sid
        self.fname = fname
        self.lname = lname
        # self.blood = blood
        self.setBlood(blood)

    def getBlood(self):
        return self.__blood  # __ is private properties

    def setBlood(self, blood):
        if blood.upper() in ['A', 'B', 'AB', 'O']:
            self.__blood = blood.upper()
        else:
            raise ValueError('Invaid blood group')

    def __str__(self):
        return "{} {}, blood group {}".format(self.fname, self.lname, self.__blood)


if __name__ == '__main__':
    s = Studen("510392", "sutin", "injitt", "AB")
    print(s)
