from cryptography.fernet import Fernet

print("File Encryption Tool:")
print("\n[+] Enter 1 if you have single file to encrypt \n[+] Enter 2 if you have multiples files to decrypt\n")
option = input("\n [-] Choose your option :")
key = input("[+] Enter Key generated from keyGenerator.py    :")
if option == "1":
    encryption_file_name = "Encrypted_data.txt"
    file_path = input("[+] Enter your file path along with file name  : ")
    
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encryption_file_name, 'wb') as f:
        f.write(encrypted)

    
elif option == "2":
    def encryption_multiple():
        with open(file_path_2, 'rb') as f:
           data2 = f.read()

        fernet2 = Fernet(key)
        encrypted2 = fernet2.encrypt(data2)
        with open(encryption_file_name, 'wb') as f:
            f.write(encrypted2)
    
    for i in range (0, 5):
        file_path_2 = input("Enter file path %d (limit 5)  :  "%i )
        encryption_file_name = "Encrypted_data%d.txt"%i
        i += 1
        encryption_multiple()
        


   
   
    
