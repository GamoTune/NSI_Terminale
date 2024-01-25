from cryptography.fernet import Fernet
import binascii

# Clé utilisée pour le chiffrement et le déchiffrement
key = b'nmXnI7JUw29F6uRm1xKJfKqwr8igayxRmJU9bao14dk='  # Assurez-vous que c'est la même clé utilisée pour le chiffrement

# Création d'une instance de Fernet avec la clé
fernet = Fernet(key)

# Données chiffrées en format hexadécimal ou autre format non-ASCII
encrypted_data = 'gAAAAABlfJghQF_5HEh7rBOfJ3ejbxvw4h6_v_9Sr9GV5eWe6ziltB5pgZCApkSp6c_krkK3XHoN9fbGZ-tRc7xz4Chi7ixWjRuDfEJ-CHAVJfKJxVrbMfEl1akaKuHHOYDnuZhfezkU'

# Conversion des données chiffrées en binaire

# Déchiffrement des données
try:
    decrypted_data = fernet.decrypt(encrypted_data)
    print("Données déchiffrées:", decrypted_data.decode())
except Exception as e:
    print("Une erreur est survenue lors du déchiffrement:", e)
