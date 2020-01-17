# Class, Contructor | __init__
class Player():
    def __init__(self):
        self.fname = ''
        self.lanme = ''
        self.nuumber = ''


class Player2:
    def __init__(self, fname="test", lname="test2", number="30"):
        self.fname = fname
        self.lname = lname
        self.number = number

    def __str__(self):  # override to string
        # return to string
        # return "fname: {} lname: {} number: {}".format(self.fname, self.lname, self.number)

        # return all variable in self
        a = vars(self)  # return data dictionary
        s = ["{:10}: {}".format(k, v)
             for k, v in a.items()]  # return key value
        return "\n".join(s)

    # def __repr__(self):  # representation
    #     attr = repr((self.fname, self.lname, self.number))
    #     return "{} {}".format(self.__class__.__name__, attr)


if __name__ == '__main__':
    p1 = Player()
    p1.fname = 'sutin'
    p1.lanme = 'injitt'
    p1.nuumber = 33
    print("class with self only: {}".format(p1.fname))

    p2 = Player2("sutin", "thinny", "20")
    print("class with self, params: {}".format(p2.fname))

    p3 = Player2()
    print("class with default params: {}".format(p3.fname))
