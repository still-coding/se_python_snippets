# Исключения:
#     1. Обработка ошибок
#     2. Уведомление о событиях
#     3. Обработка особых случаев
#     4. Действия при завершении (контексты)


try:
    pass
except Exception as e:
    raise
else:
    pass



# О.ф
#     try:
#         операторы0
#     except имя1:
#         операторы1
#     except (перечисление_имён): # любое из перечисленных
#         операторы2
#     except имяN as переменная: # экземпляр исключения связывается с переменной
#         операторы3
#     except:         # любое из оставшихся
#         операторы4
#     else:           # если не было сгенерировано исключений
#         операторы5
#     finally:        # выполняется в любом случае
#         операторы6

from e02_my_exception import MyException


def wrong_fun():
    l = tuple(range(3))

    try:
        return x + l[3]
    except NameError as exc:
        print(f'{exc}')
        return None




if __name__ == '__main__':

    # print('I used to be an adventurer like you...')
    # raise MyException

    assert False, "Nobody expects the Spanish Inquisition!" 
    print('Всё.')
