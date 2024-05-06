"""Модуль для работы с записями"""
from validator import Validator


class RecordWorker:
    """Класс для работы с записями файла"""
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.validator = Validator()

    def record_to_str(self, id: str, date: str, category: str,
                      total: str, description: str) -> str:
        """Метод для преобразования записи к строке"""
        return f"ID: {id}\n"\
               f"Дата: {date}\n"\
               f"Категория: {category}\n"\
               f"Сумма: {total}\n"\
               f"Описание: {description}\n\n"

    def load_records(self) -> list:
        """Метод для выгрузки всех записей из файла"""
        with open(self.filepath, "r", encoding="utf-8") as file:
            records: list = file.readlines()
            data: list = []
            if records:
                for i in range(0, len(records), 6):
                    id: str = records[i].replace("ID: ", "", 1)[: -1]
                    date: str = records[i + 1].replace("Дата: ", "", 1)[: -1]
                    category: str = records[i + 2].replace("Категория: ", "", 1)[: -1]
                    total: str = records[i + 3].replace("Сумма: ", "", 1)[: -1]
                    description: str = records[i + 4].replace("Описание: ", "", 1)[: -1]
                    data.append([id, date, category, total, description])
        return data

    def add_record(self) -> None:
        """Метод для добавления записи в файл"""
        id: int = len(self.load_records())
        record_data: list = self.validator.input_valid_data()

        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(self.record_to_str(id, *record_data))

        print(f"Создана запись с индексом {id}\n")

    def print_balance(self) -> int:
        """Метод для получения баланса по всем записям из файла"""
        records: list = self.load_records()
        debit = filter(lambda x: x[2] == "Доход", records)
        credit = filter(lambda x: x[2] == "Расход", records)
        result: int = sum(int(item[3]) for item in debit) - sum(int(item[3]) for item in credit)

        print(f"Ваш баланс {result}\n")

        return result

    def edit_record(self) -> None:
        """Метод для редактирования записи по id"""
        records: list = self.load_records()
        if records:
            id: int = self.validator.input_valid_id(len(records))
            record_data: list = self.validator.input_valid_data()

            records[id] = [id, *record_data]

            data: list = []
            for rec in records:
                data.append(self.record_to_str(*rec))

            with open(self.filepath, "w", encoding="utf-8") as file:
                file.writelines(data)

            print(f"Строка с индексом {id} изменена\n")
        else:
            print("В файле нет записей!")

    def search(self) -> None:
        """Метод для поиска записей по определенному критерию"""
        search_field: int = self.validator.input_valid_search_field()
        value: str = input("Введите значение по которому хотите выполнить поиск записей\n")
        records: list = self.load_records()
        filter_records: list = list(filter(lambda x: x[int(search_field)] == value, records))
        if filter_records:
            print("\nРезультаты поиска:")
            for rec in filter_records:
                print(self.record_to_str(*rec), end='')
        else:
            print("По заданным параметрам ничего не найдено!\n")
