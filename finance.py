class RecordWorker:
    """Класс для работы с записями файла"""
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_records(self):
        """Функция для выгрузки всех записей из файла"""
        with open(self.filepath, "r", encoding="utf-8") as file:
            records = file.readlines()
        return records

    def add_record(self):
        """Функция для добавления записи в файл"""
        index: int = len(self.load_records())
        date: str = input("Введите дату\n")
        category: str = input("Введите категорию\n")
        total: str = input("Введите сумму\n")
        description: str = input("Введите описание\n")

        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(f"{index}:{date}:{category}:{total}:{description}\n")

        print(f"Создана запись с индексом {index}\n")

    def print_balance(self):
        """Функция для получения баланса по всем записям из файла"""
        records: list = self.load_records()
        records_list = [record.split(":") for record in records]
        debit = filter(lambda x: x[2] == "Доход", records_list)
        credit = filter(lambda x: x[2] == "Расход", records_list)
        res: int = sum(int(item[3]) for item in debit) - sum(int(item[3]) for item in credit)

        print(f"Ваш баланс {res}\n")

    def edit_record(self):
        index: int = int(input("Введите номер записи для редактирования\n"))
        date: str = input("Введите дату\n")
        category: str = input("Введите категорию\n")
        total: str = input("Введите сумму\n")
        description: str = input("Введите описание\n")

        records: list = self.load_records()
        records[index] = f"{index}:{date}:{category}:{total}:{description}\n"

        with open(self.filepath, "w", encoding="utf-8") as file:
            file.writelines(records)

        print(f"Строка с индексом {index} изменена\n")

    def search_records(self):



rw = RecordWorker("finance.txt")

action_dict: dict = {
    "1": rw.print_balance,
    "2": rw.add_record,
    "3": rw.edit_record,
    "4": "search",
    "5": False
}