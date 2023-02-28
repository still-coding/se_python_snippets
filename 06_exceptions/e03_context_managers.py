# f = open('exceptions_hierarchy.txt', 'r')
# for line in f:
#     print(line, end='')
# f.close()

# О.ф
#     with выражение [as переменная]:
#         операторы


# with open('exceptions_hierarchy.txt', 'r') as f:
#     for line in f:
#         print(line, end='')
#
#
#
# f = open('exceptions_hierarchy.txt', 'r')
# try:
#     for line in f:
#         print(line, end='')
# finally:
#     f.close()




# Оператор with:
#     1. Выражение вычисляется, результат преобразуется в объект диспетчера контекста.
#         __enter__, __exit__
#     2. Вызывается __enter__, его возврат присваивается в переменную, указанную после as
#     3. Выполняется код блока with
#     4. При возникновении исключения вызывается __exit__(type, value, traceback)
#     5. Если исключений не возникает - метод exit всё равно вызывается после выполнения блока __exit__(None, None, None)


# Контекстный менеджер через класс

class MyContextManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        print('file was closed')



with MyContextManager('exceptions_hierarchy.txt', 'r') as f:
    for line in f:
        print(line, end='')





from datetime import datetime
import time
 
 
class Timer:
    def __init__(self): 
            pass
 
    def __enter__(self):
            self.start = datetime.utcnow()
            return None
    
    def __exit__(self, type, value, traceback):
            print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")
 
 
with Timer():
    time.sleep(2) 



# контекстный менеджер через генераторную функцию

from contextlib import contextmanager
 
 
@contextmanager
def timer():

    start = datetime.utcnow()
    # перед yeild - код, который предназначем для __enter__
    yield # если вам нужно что-то вернуть - указываем тут
    # после yeild - для __exit__
    print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")
 
 
with timer():
    time.sleep(2)