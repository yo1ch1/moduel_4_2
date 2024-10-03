def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()




def test_function(): #pycharm не находит фунцию inner_function т.к. она находится в локальной области видимости.
    def inner_function():
        print('Я в области видимости функции test_function')


inner_function()
