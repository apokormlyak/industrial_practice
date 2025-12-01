from utils import get_option, create_worker, show_workers, filter_workers


def run():
    start = True
    all_workers = []
    while start:
        option = get_option()
        if option == 1:
            new_worker = create_worker(
                input("Введите ФИО сотрудника: "),
                input("Введите зп сотрудника: "),
                input("Введите название должности сотрудника: "),
                input("Введите год трудоустройства сотрудника: ")
            )
            all_workers.append(new_worker)
        elif option == 2:
            to_show = filter_workers(
                int(input("Вы хотите увидеть всех сотрудников, работающих в компании с года: ")),
                all_workers
            )
            show_workers(to_show)
        elif option == 3:
            start = False
            print("До свидания")


if __name__ == '__main__':
    run()
