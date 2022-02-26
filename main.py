from logger import LOGS, LOGS_DIR, loger_constructor


@loger_constructor(LOGS, LOGS_DIR)
def test_foo(a, b):
    x = a * b
    return x


if __name__ == '__main__':
    test_foo(2, 5)
    test_foo(10, 2)
    test_foo(48, 9)
