from datetime import datetime
from typing import List

from worker import Worker


def create_worker(fio: str, salary: str, job_name: str, employment_year: str) -> Worker:
    """
    Метод создает объект worker
    :return:
    """
    return Worker(fio, salary, job_name, employment_year)


def filter_workers(year: int, workers: List[Worker]) -> List[Worker]:
    current_year = datetime.now().year
    return [i for i in workers if (current_year - int(i.employment_year)) >= year]


def show_workers(to_show: List[Worker]) -> None:
    if to_show:
        for worker in to_show:
            print(worker)
    else:
        print("Сотрудников, работающих более указанных лет еще нет")


def get_option() -> int:
    print(
        "Выберите, что вы хотите выполнить: \n1. Создать нового сотрудника"
        "\n2. Посмотреть список сотрудников с определенным стажем"
        "\n3. Закончить работу с программой\n"
    )
    option = input("Ваш выбор: ").strip()
    while True:
        if option in ("1", "2", "3"):
            return int(option)
        else:
            print("Выберите один из трех предложенных вариантов")