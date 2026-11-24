from operator import itemgetter


class HardDisk:
    """Жесткий диск"""
    def __init__(self, id, name, capacity_tb, interface, comp_id):
        self.id = id
        self.name = name
        self.capacity_tb = capacity_tb
        self.interface = interface
        self.comp_id = comp_id


class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class HardDiskComputer:
    """Связь жестких дисков и компьютеров для отношения многие-ко-многим"""
    def __init__(self, comp_id, disk_id):
        self.comp_id = comp_id
        self.disk_id = disk_id


# Компьютеры
computers = [
    Computer(1, 'Офисный ПК'),
    Computer(2, 'Рабочая станция'),
    Computer(3, 'Домашний ПК'),
    Computer(4, 'Сервер файлов'),
]

# Жесткие диски. comp_id реализует связь один-ко-многим.
hard_disks = [
    HardDisk(1, 'Seagate Barracuda', 2, 'SATA', 1),
    HardDisk(2, 'WD Blue', 1, 'SATA', 2),
    HardDisk(3, 'Samsung 870 EVO', 1, 'SATA', 2),
    HardDisk(4, 'Kingston NV2', 2, 'M.2 NVMe', 3),
    HardDisk(5, 'Toshiba Canvio', 4, 'USB', 4),
]

# Промежуточные записи для связи многие-ко-многим.
hard_disks_computers = [
    HardDiskComputer(1, 1),
    HardDiskComputer(4, 1),
    HardDiskComputer(2, 2),
    HardDiskComputer(1, 3),
    HardDiskComputer(2, 3),
    HardDiskComputer(3, 4),
    HardDiskComputer(1, 5),
    HardDiskComputer(4, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим.
    one_to_many = [
        (disk.name, disk.capacity_tb, comp.name)
        for comp in computers
        for disk in hard_disks
        if disk.comp_id == comp.id
    ]

    # Соединение данных многие-ко-многим.
    many_to_many_temp = [
        (disk.name, disk.interface, link.disk_id, link.comp_id)
        for disk in hard_disks
        for link in hard_disks_computers
        if disk.id == link.disk_id
    ]

    many_to_many = [
        (disk_name, interface, comp.name)
        for disk_name, interface, disk_id, comp_id in many_to_many_temp
        for comp in computers
        if comp.id == comp_id
    ]

    # Запрос Б1. Все связанные диски и компьютеры,
    # сортировка по названию жесткого диска.
    print('Задание Б1')
    res_1 = sorted(one_to_many, key=itemgetter(0))
    print(res_1)

    # Запрос Б2. Количество жестких дисков на каждом компьютере.
    print('\nЗадание Б2')
    res_2_unsorted = []
    for comp in computers:
        comp_disks = list(filter(lambda row: row[2] == comp.name, one_to_many))
        if len(comp_disks) > 0:
            res_2_unsorted.append((comp.name, len(comp_disks)))

    # Сортировка по количеству дисков (по убыванию).
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    # Запрос Б3. Диски с интерфейсом, название которого заканчивается
    # на «SATA», и названия связанных с ними компьютеров.
    print('\nЗадание Б3')
    res_3 = {}
    for disk in hard_disks:
        if disk.interface.endswith('SATA'):
            disk_computers = list(
                filter(lambda row: row[0] == disk.name, many_to_many)
            )
            comp_names = [comp_name for _, _, comp_name in disk_computers]
            res_3[disk.name] = comp_names
    print(res_3)


if __name__ == '__main__':
    main()
