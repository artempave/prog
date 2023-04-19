class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, data=None):
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
        else:
            self.tail = item
        self.head.next = item

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head == self.tail:
            raise Exception("Список пуст")
        item = self.head.next
        self.head.next = item.next
        if item.next != None:
            item.next.prev = self.head
        else:
            self.tail = self.head
        return item.data

    # метод определения длины списка
    def __len__(self):
        len_list = 0
        item = self.head.next
        while item != None:
            len_list += 1
            item = item.next
        return len_list

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

    # реализуйте метод, добавляющий новый элемент со значением x после p. Помните об указателе tail!
    def addAfter(self, p, x):
        if p == None:
            raise Exception("Указател не может быть равен None")
        item = Item(x)
        item.next = p.next
        if p.next != None:
            p.next.prev = item
        else:
            self.tail = item
        p.next = item
        item.prev = p

    # реализуйте метод удаления элемента p. Также помните об указателе tail! Он не должен "съехать"
    def remove(self, p):
        if p == None or p == self.head:
            raise Exception("Нельзя удалить фиктивную голову или None")
        p.prev.next = p.next
        if p.next != None:
            p.next.prev = p.prev
        else:
            self.tail = p.prev

    # реализуйте метод поиска элемента в списке
    def find(self, x):
        item = self.head.next
        while item != None:
            if item.data == x:
                return item
            item = item.next
        return None

        # реализуйте перегрузку индексации на чтение

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.__len__():
            raise Exception("{} вышел за диопазон списка".format(idx))
        item = self.head.next
        for _ in range(idx):
            item = item.next
        return item.data

    # реализуйте перегрузку индексации на запись
    def __setitem__(self, idx, x):
        if idx < 0 or idx >= self.__len__():
            raise Exception("{} вышел за диопазон списка".format(idx))
        item = self.head.next
        for _ in range(idx):
            item = item.next
        item.data = x

    # реализуйте перегрузку метода in (может можно воспользоваться уже реализованным find?)
    def __contains__(self, x):
        if self.find(x) == None:
            return False
        return True

    # реализуйте сложение двух списков (попробуйте использовать уже написанные методы для упрощения кода)
    def __add__(self, lst):
        sum_MyList = MyList()
        item = self.head.next
        while item != None:
            sum_MyList.append(item.data)
            item = item.next
        item = lst.head.next
        while item != None:
            sum_MyList.append(item.data)
            item = item.next
        return sum_MyList

    # реализуйте метод конкатенации двух списков. Второй список не забудьте "обнулить"
    def concat(self, lst):
        if self.head.next == None:
            self.head.next = lst.head.next
            self.tail = lst.tail
        else:
            self.tail.next = lst.head.next
            if lst.head.next != None:
                lst.head.next.prev = self.tail
            self.tail = lst.tail
        lst.head = Item()
        lst.tail = lst.head

    # метод, возвращающий итератор, мы написали за вас. Вам осталось только дописать сам класс итератора
    def __iter__(self):
        return MyListIterator(self.head.next)


class MyListIterator:
    def __init__(self, item):
        self.currentItem = item

    def __next__(self):
        # здесь необходимо написать код, который вернет значение
        # элемента, на который ссылается currentItem, и передвинет его
        # на следующий элемент. Если currentItem никуда не ссылается
        # (т.е. равен None), то необходимо выбросить исключение
        # raise StopIteration
        if self.currentItem == None:
            raise StopIteration
        item = self.currentItem
        self.currentItem = item.next
        return item.data


# Этот код менять не нужно. При корректной реализации класса MyList он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

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
if (1 in A):
    print("True")
else:
    print("False")
if (2 in A):
    print("True")
else:
    print("False")
for i in range(6, 10):
    A.append(i)
A[0] = 0
A[4] = -1
for i in range(len(A)):
    print(A[i])
for i in A:
    print(i)
A.remove(A.find(-1))
print(A)
B = MyList()
for i in range(6):
    B.append(i)
A = A + B
A.append(100)
B[0] = 100
print(A)
print(B)
A.concat(B)
A.append(100)
print(A)
print(B)
