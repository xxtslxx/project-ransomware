import os
import pyaes


#open file crypter

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name,'rb')
file_data = file.read()
file.close()

# key decrypter

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remove file crypter
os.remove(file_name)

# make new file decrypter

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
	
