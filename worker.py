class Worker:
    def __init__(self, fio: str, salary: str, job_name: str, employment_year: str):
        self._fio = fio
        self._salary = salary
        self._job_name = job_name
        self._employment_year = employment_year

    def __str__(self):
        return f"Сотрудник {self.fio}\nУровень зп {self.salary}\nЗанимает должность {self.job_name}\nРаботает в компании с {self.employment_year} года\n"

    @property
    def employment_year(self):
        return self._employment_year

    @property
    def salary(self):
        return self._salary

    @property
    def fio(self):
        return self._fio

    @property
    def job_name(self):
        return self._job_name
