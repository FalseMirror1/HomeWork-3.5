import os
from datetime import datetime

LOGS = "logs.txt"
LOGS_DIR = r"C:\Users\falsemirror\Desktop\Обучение\Домашка PY\ProPY 1.5\Logs"


def loger_constructor(file_name, logs_dir=None):
    if logs_dir is None:
        folder = os.path.join(os.getcwd())
    else:
        folder = os.path.join(os.path.abspath(logs_dir))

    logs_dir = os.path.join(folder, file_name)

    def logger_decorator(old_function):
        # Логгер записывает в файл дату и время вызова функции,
        # имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
        def new_foo(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y -- %H:%M:%S")
            foo_name = old_function.__name__
            input_data = f'Data: {args} & {kwargs}'
            output_data = old_function(*args, **kwargs)
            log_info = f'Date & Time:  {log_date} \n' \
                       f'Function name:  {foo_name} \n' \
                       f'{input_data} \n' \
                       f'Result of {foo_name}: {output_data}\n' \
                       f'{"-" * 30}\n'

            with open(logs_dir, 'a', encoding='utf-8') as f:
                f.write(log_info)

            return output_data

        return new_foo

    return logger_decorator
