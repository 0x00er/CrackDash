import os
import zipfile
import rarfile
from time import time

def cls():
    command = 'clear' if os.name == 'posix' else 'cls'
    os.system(command)


def extract_zip(zip_path, password):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
        return True
    except Exception:
        return False

def extract_rar(rar_path, password):
    try:
        with rarfile.RarFile(rar_path, 'r') as rar_file:
            rar_file.extractall(pwd=password.encode('utf-8'))
        return True
    except Exception:
        return False
    

def main(file_path, word_list):
    if file_path.lower().endswith('.zip'):
        extract_function = extract_zip
    elif file_path.lower().endswith('.rar'):
        extract_function = extract_rar
    else:
        print(" [!] Unsupported file format. Supported formats: ZIP and RAR.")
        quit()

    try:
        with open(word_list, "rb") as f:
          passwords = [line.decode('latin-1').strip() for line in f.readlines()]



        c_t = time()
        for i, password in enumerate(passwords, start=1):
            if extract_function(file_path, password):
                t_t = time() - c_t
                print("\n [*] Password Found :)\n" + " [*] Password: " + password + "\n")
                print(" [***] Took %f seconds to crack the password. That is, %i attempts per second." % (t_t, i / t_t))
                quit()

        print(" [X] Sorry, Password Not Found :(")
    except Exception as e:
        print(f" [!] Error: {e}")
    finally:
        quit()

cls()

banner = '\n #######################################\n'
banner += ' # CrackDash                           #\n'
banner += ' #######################################\n'
banner += ' # A lightweight tool for blazing-fast #\n'
banner += ' # ZIP and RAR password cracking using #\n'
banner += ' # password list!                      #\n'
banner += ' #######################################\n'
banner += ' # Coded By 0x00er                     #\n'
banner += ' # x.com/0x00er                        #\n'
banner += ' #######################################\n'
banner += ' GitHub:\n'
banner += ' https://github.com/0x00er/CrackDash/\n\n'
banner += ' [1] CrackDash\n'
banner += ' [0] Exit\n'
print(banner)

a = input(" [?] Enter Number : ")

if a == '0':
    cls()
    print(" [!] No refunds, choom :)")
    quit()
elif a == '1':
    import zipfile
    from time import time

    cls()

    textzippass = '''
    #########################################
    #              CrackDash                #
    #########################################
    # 0x00er                                #
    # github.com/0x00er                     #
    # x.com/0x00er                          #
    #########################################
    '''
    print(textzippass)

    file_path = input(" [@] File Address: ")
    print("")

    word_list = input(" [@] Password List Address: ")

    main(file_path, word_list)
