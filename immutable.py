def immutable_demo():
    n = 5
    print("id(n) = {}, n= {}".format(id(n), n))

    n = n + 4
    print("id(n) = {}, n= {}".format(id(n), n))

    s = "sutin injitt"
    print("id(n) = {}, n= {}".format(id(s), s))


if __name__ == '__main__':
    print(immutable_demo())
