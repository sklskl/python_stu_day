class people:
    name = ''
    sex = 0
    __height = 0

    def __init__(self, n, a, w):
        self.name = n
        self.sex = a
        self.__height = w

    def speak(self):
        print("%s说我的性别是%s。".format(self.name, self.sex))


class son(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("{}说我的性别是{},我在读{}年纪。".format(self.name, self.sex, self.grade))


s = son('skl', '女', 12, 6)
s.speak()


# def user(your_name):
#     name = your_name
#     print('hello,' + name)
#
#
# user('skl')
#     File Object = open()
