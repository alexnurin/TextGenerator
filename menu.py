
print("Это консольное приложение")

while True:
    print("Введите команду. Введите 'help' для получения команд")
    cmd = input()
    if cmd == 'help':
        print('help - помощь')
        print('read - сканирование Вашего текста')
        print('gen - генерация и вывод текста')
        print('exit - закрытие программы')
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
        scan.write(a)
        scan.close()
        print(a)
        import scaner
        print('Успех')
    elif cmd == 'gen' or cmd == 'write':
        exec(open("generator.py").read())
        gen = open('output.txt', 'r')
        text = gen.read()
        gen.close()
        print("Сгенерированный текст:\n" + text)

    else:
        print('Неизвестная команда.')
