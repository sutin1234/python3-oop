# double underscore -> dunder
class Alpha:
    normal = 1
    _lucky = 13
    __secret = 999  # name mangle -> change to _classname__attriute


if __name__ == '__main__':
    a = Alpha
    print(a.normal)
    print(a._lucky)
    # print(a.__secret)

    # show data dictionary
    print(a.__dict__)
    print(a._Alpha__secret)
