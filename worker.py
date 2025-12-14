class Worker:
    def __init__(self, fio: str, salary: str, job_name: str, employment_year: str):
        self.fio = fio
        self.salary = salary
        self.job_name = job_name
        self._employment_year = employment_year

    def __str__(self):
        return f"Сотрудник {self.fio}\nУровень зп {self.salary}\nЗанимает должность {self.job_name}\nРаботает в компании с {self.employment_year} года\n"

    @property
    def employment_year(self):
        return self._employment_year
