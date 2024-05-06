"""Модуль для работы с записями"""
from validator import Validator


class RecordWorker:
    """Класс для работы с записями файла"""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.validator = Validator()

    def record_to_str(self, id, date, category, total, description):
        """Функция для преобразования записи к строке"""
        return f"ID: {id}\n"\
               f"Дата: {date}\n"\
               f"Категория: {category}\n"\
               f"Сумма: {total}\n"\
               f"Описание: {description}\n\n"

    def load_records(self) -> list:
        """Функция для выгрузки всех записей из файла"""
        with open(self.filepath, "r", encoding="utf-8") as file:
            records: list = file.readlines()
            data: list = []
            if records:
                for i in range(0, len(records), 6):
                    id = records[i].replace("ID: ", "", 1)[: -1]
                    date = records[i + 1].replace("Дата: ", "", 1)[: -1]
                    category = records[i + 2].replace("Категория: ", "", 1)[: -1]
                    total = records[i + 3].replace("Сумма: ", "", 1)[: -1]
                    description = records[i + 4].replace("Описание: ", "", 1)[: -1]
                    data.append([id, date, category, total, description])
        return data

    def add_record(self) -> None:
        """Функция для добавления записи в файл"""
        id: int = len(self.load_records())
        record_data: list = self.validator.input_valid_data()

        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(self.record_to_str(id, *record_data))

        print(f"Создана запись с индексом {id}\n")

    def print_balance(self):
        """Функция для получения баланса по всем записям из файла"""
        records: list = self.load_records()
        records_list = [record.split(":") for record in records]
        debit = filter(lambda x: x[2] == "Доход", records_list)
        credit = filter(lambda x: x[2] == "Расход", records_list)
        result: int = sum(int(item[3]) for item in debit) - sum(int(item[3]) for item in credit)

        print(f"Ваш баланс {result}\n")

    def edit_record(self):
        """Функция для редактирования записи по id"""
        records: list = self.load_records()
        id: int = self.validator.input_valid_id(len(records))
        record_data: list = self.validator.input_valid_data()

        records[id] = self.record_to_str(id, *record_data)

        with open(self.filepath, "w", encoding="utf-8") as file:
            file.writelines(records)

        print(f"Строка с индексом {id} изменена\n")

    def search(self):
        """Функция по поиску записей по определенному критерию"""
        n: str = input("Выберите по какому значению будете выполнять поиск (цифра от 1 до 5):\n"
                       "1. ID\n"
                       "2. Дата\n"
                       "3. Категория\n"
                       "4. Сумма\n"
                       "5. Описание\n")
        value: str = input("Введите значение по которому хотите выполнить поиск записей\n")
        records: list = self.load_records()
        filter_records: list = list(filter(lambda x: x[int(n)-1] == value, records))
        if filter_records:
            print("\nРезультаты поиска:")
            for rec in filter_records:
                print(self.record_to_str(rec[0], rec[1], rec[2], rec[3], rec[4]), end='')
        else:
            print("По заданным параметрам ничего не найдено!\n")
