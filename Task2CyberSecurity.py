operation=input("Enter E if you wish to Encrypt/Enter D if you choose to Decrypt").lower()
if operation=='e':
    try:
        path=input(r'Enter path of Image : ')
        key=int(input('Enter Key for encryption of Image : '))
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
              image[index] = values ^ key
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
    except Exception:
        print('Error caught : ', Exception.__name__)
elif operation=='d':
    try:
        path = input(r'Enter path of Image : ')
        key = int(input('Enter Key for encryption of Image : '))
        print('The path of file : ', path)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
              image[index] = values ^ key
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')
        
    except Exception:
        print('Error caught : ', Exception.__name__)

