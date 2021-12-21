import secrets
from os import system

privatekey = secrets.token_urlsafe(8)

def cipher(mode):
    mes = ''
    if mode:
        mes = 'Encrypted text: '
    if not mode:
        mes = 'Decrypted text: '
    bin_text = ''
    while len(bin_text) < len(privatekey):
        bin_text = input("Enter text (length > %d): " % (len(privatekey) + 1))
    bin_key = ''
    while len(bin_key) != len(privatekey):
        bin_key = input("Enter key (length = %d): " % (len(privatekey)))
    Z = '' + privatekey
    schetchik = 0
    while len(Z) != len(bin_text):
        a = 0
        for count, c in enumerate(bin_key):
            # cipher here current bit here
            a ^= ord(c) * ord(Z[schetchik + count])
        Z += chr(a)
        schetchik += 1
    Y = ''
    for count, z in enumerate(Z):
        # feedback bit
        Y += chr(ord(z) ^ ord(bin_text[count]))
    print(mes, Y)


def main():
    menu = '''
   ------------Menu-------------
   1 - Зашифровать сообщение
   2 - Расшифровать сообщение
   -----------------------------
                       q - Выход
   '''

    while True:
        answer = input(menu)
        if str(answer).lower() == 'q':
            exit()

        elif answer == '1':
            cipher(True)

        elif answer == '2':
            cipher(False)

        else:
            system('cls')
        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == '__main__':
    main()
