"""
Точка входа в приложение, создает бесконечный цикл в котором пользователь
вызывает необходимые ему функции для работы с кошельком, посредством ввода
номера интересующего его действия
"""
from finance import RecordWorker

if __name__ == "__main__":
    rw = RecordWorker("finance.txt")

    action_dict: dict = {
        "1": rw.print_balance,
        "2": rw.add_record,
        "3": rw.edit_record,
        "4": rw.search,
        "5": False
    }

    while True:
        print("1. Вывести баланс\n2. Добавить запись\n3. Редактировать запись"
              "\n4. Поиск записей\n5. Выход")
        try:
            action = action_dict[input()]
            if action is False:
                break
            action()
        except KeyError:
            print("\nОшибка!!! Введите номер пункта(цифра от 1 до 5)\n")
