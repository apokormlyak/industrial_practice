import random

import pytest
from faker import Faker

from utils import create_worker, filter_workers
from worker import Worker

fake = Faker("ru_RU")


def test_create_worker():
    fio = fake.name()
    job = fake.job()
    salary = str(random.randint(150000, 350000))
    year = str(fake.date_between(start_date="-10y", end_date="today").year)
    worker = create_worker(fio, salary, job, year)
    assert worker.job_name == job
    assert worker.fio == fio
    assert worker.salary == salary
    assert worker.employment_year == year


@pytest.mark.parametrize(
    "year, workers_list, result",
    [
        (1, [], []),
        (1, [Worker("fio", "230000", "job_name", "2025")], []),
        (1, [Worker("fio", "230000", "job_name", "2024")], [Worker("fio", "230000", "job_name", "2024")]),
        (1, [Worker("fio1", "230000", "job_name1", "2024"),
             Worker("fio2", "330000", "job_name2", "2025")
             ], [Worker("fio1", "230000", "job_name1", "2024")]),
        (0, [Worker("fio1", "230000", "job_name1", "2024"),
             Worker("fio2", "330000", "job_name2", "2025")
             ],
         [Worker("fio1", "230000", "job_name1", "2024"),
             Worker("fio2", "330000", "job_name2", "2025")
             ]
 ),
    ]
)
def test_filter_workers(year, workers_list, result):
    filtered_workers = filter_workers(year, workers_list)
    for num, worker in enumerate(filtered_workers):
        assert worker.salary == result[num].salary
        assert worker.fio == result[num].fio
        assert worker.job_name == result[num].job_name
        assert worker.employment_year == result[num].employment_year
