import os, time
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
    print('[1] torchok on//off\t[2] photik\t[1337] exit\n[3] battery statusisi\t[4] geolocation\t[5] brightness\n[6] contact list\t[7] vibrate')
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
    elif a == 4:
        #print(os.system('termux-location'))
        print('\033[31mnow this is not working')
        l = input('press enter to continue... ')
    elif a == 5:
        while True:
            b = input('write brightness (from 1 to 254)')
            if b.isdigit() is True:
                b = int(b)
                if 0 < b and b < 255:
                    os.system(f'termux-brightness {b}')
                    break
                else:
                    print('retry')
                    print()
            else:
                print('retry')
                print()
    elif a == 6:
        os.system('termux-contact-list > contacts_list')
        with open('contacts_list', 'r') as f:
            spisok = f.read()[14:]
            while spisok.find(':') != -1:
                spisok = spisok[spisok.find(':') + 3:]
                name = spisok[:spisok.find('"')]
                spisok = spisok[spisok.find(':') + 3:]
                nums = spisok[:spisok.find('"')]
                print(f'contact: {name}\nnumber: {nums}')
                print()
        l = input('continue... ')
    elif a == 7:
        print()
        print('[1] произвольная\t[2] sim sms\t[3] sim call')
        vibr = int(input('input: '))
        if vibr == 1:
            durat = int(input('write duration in ms: '))
            os.system(f'termux-vibrate -d {durat}')
        elif vibr == 2:
            for _ in range(2):
                os.system('termux-vibrate -d 300')
                #time.sleep(0.05)
    print('\033[0m\033[0m')
os.system('clear')
