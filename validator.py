"""Модуль для валидации данных записей при вводе и редактировании"""
import datetime


class Validator:
    """Класс для валидации данных записи"""
    def input_valid_data(self):
        """Функция для валидации даты, категории, суммы, описания"""
        flag = True
        while flag:
            date: str = input("Введите дату\n")
            try:
                datetime.date.fromisoformat(date)
                flag = False
            except ValueError:
                print("Неправильный формат данных, должен быть 'YYYY-MM-DD'.")
        flag = True
        while flag:
            category: str = input("Введите категорию\n")
            if category in ["Расход", "Доход"]:
                flag = False
            else:
                print("Неправильный формат данных, категория должна быть 'Расход' или 'Доход'.")
        flag = True
        while flag:
            total: str = input("Введите сумму\n")
            try:
                if int(total) > 0 and total[0] != "0":
                    flag = False
            except ValueError:
                print("Неправильный формат данных, сумма должна быть положительным числом.")
        description: str = input("Введите описание\n")
        return [date, category, total, description]

    def input_valid_id(self, length):
        """Функция для валидации id записи для редактирования"""
        flag = True
        while flag:
            id: str = input("Введите номер записи для редактирования\n")
            try:
                if int(id) in range(0, length):
                    flag = False
            except ValueError:
                print(f"Некорректный id, должен быть числом от 0 до {length}")
        return int(id)

