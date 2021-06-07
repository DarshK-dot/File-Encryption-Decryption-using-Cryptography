from cryptography.fernet import Fernet

key = input("Enter the same key used for Encryption  :")

file = 'decrypted data.txt'

file_path = input("enter file path along with file name  : ")


with open(file_path, "rb") as f:
    data = f.read()
        
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

with open(file, "wb") as f:
        f.write(decrypted)
