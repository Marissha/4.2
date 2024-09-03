def test_funtion():
    def inner_function():
        print('Я в бласти видимости функции test_function')

    inner_function()

test_funtion()

inner_function()