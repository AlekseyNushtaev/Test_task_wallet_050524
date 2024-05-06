"""Модуль для тестирования основных функций приложения"""
import pytest

from finance import RecordWorker


class TestRecordWorker:
    """Класс для тестирования основных функций приложения"""

    def setup_method(self) -> None:
        """Метод для инициализации"""
        self.rw = RecordWorker("test_finance.txt")

    def cancel_method(self):
        with open("test_finance.txt", "w") as file:
            file.write("")

    def test_init(self) -> None:
        """Тест метода инициализации класса"""
        assert self.rw.filepath == "test_finance.txt"

    def test_load_records(self) -> None:
        """Тест метода выгрузки данных из файла"""
        with open("test_finance.txt", "w", encoding="utf-8") as file:
            file.write(f"ID: 0\n"\
                    f"Дата: 2023-05-12\n"\
                    f"Категория: Доход\n"\
                    f"Сумма: 1000\n"\
                    f"Описание: Зарплата\n\n")
            file.write(f"ID: 1\n"\
                    f"Дата: 2023-05-12\n"\
                    f"Категория: Расход\n"\
                    f"Сумма: 900\n"\
                    f"Описание: Продукты\n\n")

        records: list = self.rw.load_records()
        assert records == [["0", "2023-05-12", "Доход", "1000", "Зарплата"],
                           ["1", "2023-05-12", "Расход", "900", "Продукты"]]

    def test_print_balance(self) -> None:
        """Тест метода для вывода баланса"""
        balance: int = self.rw.print_balance()
        self.cancel_method()
        assert balance == 100
