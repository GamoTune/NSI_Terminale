from cryptography.fernet import Fernet
import base64

key = "Pld6qfgQgjh6BUhWbv1uXXQdBBT73-Svcctk5_8znuQ="

print(key)

fernet = Fernet(key)
 
# opening the encrypted file
with open('flag.notes', 'rb') as enc_file:
    encrypted = enc_file.read()
 

decrypted = fernet.decrypt(encrypted)
 
with open('sortie.txt', 'wb') as dec_file:
    dec_file.write(decrypted)