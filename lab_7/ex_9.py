class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.mas = [None] * 10
        self.tail = -1
        self.head = 0

    # метод добавления элемента в очередь
    def enqueue(self, x):
        k = (self.tail + 1) % 10
        if self.mas[k] == None:
            self.tail = k
            self.mas[self.tail] = x
            return True
        return False

    # метод удаления элемента из очереди
    def dequeue(self):
        if self.mas[self.head] != None:
            result = self.mas[self.head]
            self.mas[self.head] = None
            self.head = (self.head + 1) % 10
            return result
        return None

    # метод для определения, пуста ли очередь
    def isEmpty(self):
        return self.mas[self.head] == None


# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
A = MyQueue()
print(A.isEmpty())
A.enqueue(1)
A.enqueue(2)
print(A.dequeue())
A.enqueue(3)
print(A.dequeue())
A.enqueue(4)
A.enqueue(5)
print(A.isEmpty())
A.enqueue(6)
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.isEmpty())
A.enqueue(10)
A.enqueue(11)
A.enqueue(12)
A.enqueue(13)
A.enqueue(14)
A.enqueue(15)
A.enqueue(16)
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())