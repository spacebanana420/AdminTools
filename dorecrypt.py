import os, math, secrets, sys

def encrypt_openssl(operation, file): #requires checking if its a folder
    password = input("Input password ")
    if operation == 1:
        command = 'openssl enc -e -in ' + file + ' -k ' + password + ' -pbkdf2 -aes256 -out ' + file + '.doremy'
    else:
        file_nodoremy = file.replace(".doremy" "")
        command = 'openssl enc -d -in ' + file + ' -k ' + password + ' -* -out ' + file_nodoremy
    os.system(command)

def encrypt_zip(operation, file):
    if operation == 3:
        command = 'zip -r -3 -v -e "' + file + '.dorezip" "' + file + '"'
    else:
        command = 'zip -v "' + file + '"'
    os.system(command)

#Main
if len(sys.argv) >= 2:
    if os.path.exists(sys.argv[1]) == False:
        file = input("Input a file name ")
    else:
        file = sys.argv[1]
else:
    file = input("Input a file name ")
if os.path.exists(file) == False:
    print("The specified file/directory does not exist")
else:
    print("1: Encrypt (openssl)     2: Decrypt (openssl)"); print("3: Encrypt (zip)     4: Decrypt (zip)")
    operation = int(input("Choose an operation or type 0 to exit"))
    match operation:
        case 0: break;
        case 1 or 2: encrypt_openssl(operation, file);;
        case 3 or 4: encrypt_zip(operation, file);
        case other: print("You need to choose an operation!");
