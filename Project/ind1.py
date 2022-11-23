#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Платёж.
    plats = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о переводе.
            raspl = input("Расчётный счёт получателя: ")
            raspol = input("Расчётный счёт платильщика: ")
            sum = input("Перечисляемая сумма в руб: ")

            # Создать словарь
            plat = {
                'raspl': raspl,
                'raspol': raspol,
                'sum': sum,
            }

            # Добавить словарь в список.
            plats.append(plat)
            # Отсортировать список в случае необходимости.
            if len(plats) > 1:
                plats.sort(key=lambda item: item.get('raspl', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 35,
                '-' * 45,
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^35} | {:^45} |'.format(
                    "No",
                    "Расчётный счет получателя",
                    "Расчётный счёт платильщика",
                    "Перечисляемая сумма в руб"
                )
            )
            print(line)

            # Вывести данные о всех счетах
            for idx, plat in enumerate(plats, 1):
                print(
                    '| {:>4} | {:<30} | {:<35} | {:>45} |'.format(
                        idx,
                        plat.get('raspl', ''),
                        plat.get('raspol', ''),
                        plat.get('sum', '')
                    )
                )

            print(line)

        elif command.startswith('select '):

            # Разбить команду на части для выделения пункта назначения.
            part = command.split(' ', maxsplit=1)
            com = part[1]

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения счетов из списка.
            for plat in plats:
                if com == plane.get('typ', ''):
                    count += 1
                    print(
                        '{:>4}. Расчётный счёт платильщика: {}; Перечисляемая сумма: {}'.format(count, plane.get('raspol', ''),
                                                             plat.get('sum', ''))
                    )

            # Если счетчик равен 0, то самолеты не найдены.
            if count == 0:
                print("Заданный тип не обнаружен.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - Расчётный счёт;")
            print("list - вывести список счётов;")
            print("select <тип> - запросить счета данного типа;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)