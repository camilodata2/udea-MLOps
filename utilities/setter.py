import os
import base64

def main():
    key = os.environ.get("SERVICE_ACCOUNT_KEY")

    if key is not None:
        with open('path.json', 'wb') as json_file:
            json_file.write(base64.b64decode(key))
        print(os.path.realpath('path.json'))
    else:
        print("La variable SERVICE_ACCOUNT_KEY no está definida en el entorno.")

if __name__ == '__main__':
    main()


#ahora vamos crear una credencial que nos permita conectarnos a cloud run,store and defact reyestry