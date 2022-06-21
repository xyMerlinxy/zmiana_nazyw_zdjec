import sys
import os.path
from datetime import datetime

extensions = [".png", ".jpg", ".jpeg", ".mp4", ".gif", ".bmp", ".webp", ".mp4"]

path = os.getcwd()

args = sys.argv

if len(args) == 1 or args[1] in ["-h" ,"-help" ,"--h" ,"--help"]:
    print("Program słóży do zmiany nazwy plików na foramt:")
    print("ROK-MIESIĄC-DZIEŃ GODZINA-MINUTA-SEKUNDA-MILISEKUNDA AUTOR")
    print("Nazwę autora należy podać jako pierwszy argument wywolania programu")
    print("Program zmienia nazwy plików tylko w katalogu w którym został uruchomiony")
    print("Domyślnie działa na plikach o rozszerzeniach: " +", ".join(extensions))
    print("Jeśli chcesz dodać dodatkowe rozszerzenie proszę je podać jako kolejne argumenty")
    print("Dodatkowe rozszerzenie musi zaczynać się od kropki")
    sys.exit(0)

author_name = args[1]

for extension in args[2:]:
    if extension[0] == ".":
        extensions.append(extension)
    else:
        print("Niepoprawne rozszerznie:", repr(extension))
        sys.exit(1)

for root, dirs, files in os.walk(path):
    # dirs - foldery w katalogu
    # files - pliki w aktualnym folderze
    for file in files:
        fileName, fileSuffix = os.path.splitext(file)
        if fileSuffix.lower() in extensions:
            # print(file)

            data = os.path.getmtime(file)
            data_str = datetime.utcfromtimestamp(data).strftime('%Y-%m-%d %H-%M-%S-%f')
            # print(data_str)

            counter = 0
            while True:
                try:
                    new_name = data_str + " " + author_name + ("" if counter == 0 else f"_{counter}") + fileSuffix
                    os.rename(file, new_name)
                    break
                except FileExistsError as e:
                    counter += 1

    sys.exit(0)