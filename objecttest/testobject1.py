class people:
    __name = 'jack'
    __age = 12

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

p = people()
print p.getName(),p.getAge()