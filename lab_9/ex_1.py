def calculate_ops(ops):
    # в качестве стека будем использовать обычный питоновский список
    stack = []
    # перебираем все элементы ops и вычисляем значение в соответствии с алгоритмом
    book = {
        "*":lambda x, y: x * y,
        "+":lambda x, y: x + y,
        "-":lambda x, y: y - x,
        "/":lambda x, y: y // x if x != 0 else None,
        "**":lambda x, y: y ** x
    }
    operetion = ["*", "/", "+", "-", "**"]
    for element in ops:
        if element.isdigit():
            stack.append(int(element))
        if element in operetion:
            if len(stack) < 2:
                return "error"
            x = stack.pop()
            y = stack.pop()
            fun = book[element]
            k = fun(x, y)
            if k != None:
                stack.append(k)
            else:
                return "error"
    # после того, как все прочитано, на стеке должно быть ровно одно значение - результат
    # если это так, то возвращаем его, иначе возвращаем ошибку
    if len(stack) != 1:
        return "error"
    return stack[0]
# считываем строку и делим ее на лексемы
ops = input().split()

# вычисляем результат и печатаем его
result = calculate_ops(ops)
print(result)