# static method
class Studen:
    def __init__(self, name, lname, w_kg, h_cm):
        self.name = name
        self.lname = lname
        self.w_kg = w_kg
        self.h_cm = h_cm

    @staticmethod
    def kg_pound(kg):
        return kg * 2.20462
        


if __name__ == '__main__':
    s = Studen("sutin", "injitt", 10, 30)
    print(s.kg_pound(20))
