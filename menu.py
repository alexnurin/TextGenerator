
newString = 100
n = 30
start = open("input.txt", 'w')
start.write('')
start.close()
exec(open("generator.py").read())
exec(open("scaner.py").read())
while True:
    print("Введите команду. Введите 'help' для получения команд")
    cmd = input()
    if cmd == 'help':
        print('help - помощь')
        print('read - сканирование Вашего текста')
        print('gen - генерация и вывод текста')
        print('exit - закрытие программы')
        print('set - настройки')
    elif cmd == 'set':
        print('Настоящие настройки: ')
        print('Количество слов в генерации -', n)
        print('Новая строка каждые', newString, "слов")
        print('Введите "words" или "strings", чтобы изменить соответствующий параметр или выйти')
        cmd_set = input()
        if cmd_set == 'words':
            print("Введите новое число слов в генерации:")
            n = int(input())
            print("Успех. Теперь слов в генерации -", n)
        elif cmd_set == 'strings':
            print("Введите, через сколько слов будет ставиться перенос строки:")
            newString = int(input())
            print("Успех. Теперь новая строка каждые", newString, "слов")
        print("Выход из настроек")
    elif cmd == 'close' or cmd == 'exit':
        exit(0)
    elif cmd == 'read' or cmd == 'scan':
        print('Введите текст прямо сюда. Закончите ввод строкой "end" без кавычек')
        a = ''
        text = input()
        while text != 'end':
            a += text + " "
            text = input()
        print("Сканирование...")
        scan = open("input.txt", 'w', encoding='utf-8')
        exec(open("scaner.py").read())
        scan.write(a)
        scan.close()
        print(a)
        print('Успех')
    elif cmd == 'gen' or cmd == 'write':
        exec(open("generator.py").read())
        gen = open('output.txt', 'r')
        text = gen.read()
        gen.close()
        print("Сгенерированный текст:\n" + text)

    else:
        print('Неизвестная команда.')
