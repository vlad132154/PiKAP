# используется для сортировки
from operator import itemgetter


class Program:
    """Программа"""
    def __init__(self, id, name, developer, size_mb, comp_id):
        self.id = id
        self.name = name
        self.developer = developer
        self.size_mb = size_mb
        self.comp_id = comp_id


class Comp:
    """Компьютер"""
    def __init__(self, id, name, processor, ram_gb):
        self.id = id
        self.name = name
        self.processor = processor
        self.ram_gb = ram_gb


class ProgramComp:
    """
    Связь «Программа - Компьютер» для реализации
    отношения многие-ко-многим
    """
    def __init__(self, comp_id, program_id):
        self.comp_id = comp_id
        self.program_id = program_id


# Компьютеры
comps = [
    Comp(1, 'Компьютер разработчика', 'Intel Core i7', 16),
    Comp(2, 'Графическая рабочая станция', 'AMD Ryzen 7', 32),
    Comp(3, 'Офисный компьютер', 'Intel Core i5', 16),
    Comp(4, 'Сервер приложений', 'AMD EPYC', 64),
]

# Программы
programs = [
    Program(1, 'PyCharm', 'Иванов', 1200, 1),
    Program(2, 'Blender', 'Петров', 900, 2),
    Program(3, 'GIMP', 'Сидоренко', 250, 3),
    Program(4, '7-Zip', 'Смирнов', 10, 3),
    Program(5, 'Visual Studio', 'Орлов', 1800, 4),
]

# Связь многие-ко-многим
programs_comps = [
    ProgramComp(1, 1),
    ProgramComp(4, 1),
    ProgramComp(2, 2),
    ProgramComp(4, 2),
    ProgramComp(3, 3),
    ProgramComp(1, 3),
    ProgramComp(1, 4),
    ProgramComp(3, 4),
    ProgramComp(4, 5),
    ProgramComp(1, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [
        (p.name, p.developer, c.name)
        for c in comps
        for p in programs
        if p.comp_id == c.id
    ]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [
        (p.name, p.developer, pc.comp_id, pc.program_id)
        for p in programs
        for pc in programs_comps
        if p.id == pc.program_id
    ]

    many_to_many = [
        (program_name, developer, c.name)
        for program_name, developer, comp_id, program_id
        in many_to_many_temp
        for c in comps
        if c.id == comp_id
    ]

    print('Задание Б1')
    # Сортировка по названию программы (первый элемент кортежа)
    res_1 = sorted(one_to_many, key=itemgetter(0))
    print(res_1)

    print('\nЗадание Б2')
    res_2_unsorted = []
    # Перебираем все компьютеры
    for c in comps:
        # Список программ компьютера
        c_programs = list(filter(lambda i: i[2] == c.name, one_to_many))
        # Если на компьютере есть связанные программы
        if len(c_programs) > 0:
            # Количество программ на компьютере
            c_count = len(c_programs)
            res_2_unsorted.append((c.name, c_count))

    # Сортировка по количеству программ (по убыванию)
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Б3')
    res_3 = {}
    # Отбираем программы, разработчик которых имеет фамилию на «ов»
    for p in programs:
        if p.developer.endswith('ов'):
            # Список компьютеров, связанных с данной программой
            p_comps = list(filter(lambda i: i[0] == p.name, many_to_many))
            # Только названия компьютеров
            comp_names = [comp_name for _, _, comp_name in p_comps]
            # Ключ - название программы, значение - список компьютеров
            res_3[p.name] = comp_names
    print(res_3)


if __name__ == '__main__':
    main()
