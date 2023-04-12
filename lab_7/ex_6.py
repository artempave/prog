class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class MyList:
    # конструктор, который корректно инициализирует голову и хвост списка
    def __init__(self):
        self.head = Item()
        self.tail = self.head

    # метод добавления элемента в конец списка
    def append(self, x):
        item = Item(x)
        item.prev = self.tail
        self.tail.next = item
        self.tail = item

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self):
        if self.__str__() == "[]":
            raise Exception("Список пуст")
        item = self.tail
        self.tail = item.prev
        self.tail.next = None
        return item.data

    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x):
        item = Item(x)
        item.next = self.head.next
        item.prev = self.head
        if self.head.next != None:
            self.head.next.prev = item
        self.head.next = item

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.__str__() == "[]":
            raise Exception("Список пуст")
        item = self.head.next
        self.head.next = item.next
        if item.next != None:
            item.next.prev = self.head
        return item.data

    # метод определения длины списка
    def __len__(self):
        len_list = 0
        item = self.head.next
        while item != None:
            len_list += 1
            item = item.next
        return count

    # метод конструирования строкового представления списка
    def __str__(self):
        result = "["
        item = self.head.next
        while item != None:
            result += str(item.data)
            if item.next != None:
                result += ", "
            else:
                break
            item = item.next
        result += "]"
        return result

# Этот код менять не нужно. При корректной реализации класса MyList он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
"""
A = MyList()
A.append(1)
A.pushFirst(3)
A.append(5)
A.append(1)
A.pushFirst(5)
print(A)
print(A.popFirst())
print(A.pop())
print(A)
print(len(A))
"""