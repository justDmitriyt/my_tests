import os
os.system('termux-camera-photo -c 1 storage/dcim/logs/logined.jpeg')
torch = 0
i = 0
while True:
    os.system('clear')
    print("\033[31m            _             _")
    print('   __ _ ___| |_ _ __ __ _| |')
    print("  / _` / __| __| '__/ _` | |")
    print(" | (_| \\__ \\ |_| | | (_| | |")
    print("  \\__,_|___/\\__|_|  \\__,_|_|\033[0m")
    print()
    print('\033[34m\033[5mthis is not very useful staff, but i hipe you like it')
    print('[1] torchok on//off\t[2] photik\t[1337] exit\n[3] battery statusisi')
    print()
    while True:
        try:
            a = int(input('vvedite chislo int: '))
        except ValueError:
            pass
        else:
            break
    if a == 1:
        if torch == 0:
            print()
            print('Torchok228 activated')
            print()
            os.system('termux-torch on && clear')
            torch = 1
        else:
            print()
            print('Torchok228 deactivated')
            print()
            os.system('termux-torch off && clear')
            torch = 0
    elif a == 1337:
        break
    elif a == 2:
        print()
        print('camera id? 0-back, 1-front')
        print()
        cid = int(input())
        os.system(f'termux-camera-photo -c {cid} storage/dcim/new_photo{i}.jpeg')
        i += 1
    elif a == 3:
        os.system('termux-battery-status > battery')
        file = open('battery', '+r')
        text = file.read()
        health = text[text.find(':') + 3:text.find(',') - 1]
        text = text[text.find(',') + 2:]
        power = text[text.find(':') + 1:text.find(',')]
        text = text[text.find(',') + 2:]
        plug = text[text.find(':') + 1:text.find(',')]
        text = text[text.find(',') + 2:]
        text = text[text.find(',') + 2:]
        temp = int(float(text[text.find(':') + 2:text.find(',')]))
        print()
        print(f'убиваемость {health}\nпироцентики {power}\n{"не всунуто" if plug.strip() == '"UNPLUGGED"' else "всунуто"}\nтемпературики {temp}')
        print()
        l = input('press enter to continue... ')
    print('\033[0m\033[0m')
os.system('clear')
