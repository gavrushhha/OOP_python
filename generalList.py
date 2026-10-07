"""Общий список сущностей-наследников general."""


class generalList:
    def __init__(self):
        self.__list = []

    def clear(self):
        self.__list = []

    def findByCode(self, code):
        for item in self.__list:
            if item.getCode() == code:
                return item

    def getNewCode(self):
        codes = self.getCodes()
        if codes:
            return max(codes) + 1
        return 1

    def getCodes(self):
        return [item.getCode() for item in self.__list]

    def getItems(self):
        return list(self.__list)

    def appendItem(self, item):
        self.__list.append(item)

    def removeItem(self, code):
        item = self.findByCode(code)
        if item is not None:
            self.__list.remove(item)
            return True
        return False
