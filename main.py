from tasks import task_16, task_19_dec, task_19_enc


if __name__ == "__main__":
    print('1 - Поиск максимального потока и минимального разреза\n2 - Получение кода Прюфера из графа\n3 - Получение графа из кода Прюфера')
    task_number = input('Введите номер задачи, которую хотите решить: ')
    while task_number:
        if task_number == '1':
            task_16.main()
        elif task_number == '2':
            task_19_enc.main()
        elif task_number == '3':
            task_19_dec.main()
        else:
            print('Вы ввели неверный код задачи, чтобы выйти из программы оставьте поле пустым')
        task_number = input('Введите номер задачи, которую хотите решить: ')