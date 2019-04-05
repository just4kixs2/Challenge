from zipfile import ZipFile
import time

NumberPasswords = 100

filename = 'passwords/passwords'+str(NumberPasswords)+'.txt'	#define password list file
file = open(filename,'r')	#open file for reading

passwords = [line.rstrip('\n') for line in file] # read line by line and strip newline characters

starttime = time.time()

for i in passwords:
	zip_archive = ZipFile('archive1.zip')
	try:
		zip_archive.extractall(pwd=i)
	except:
		pass
	zip_archive = ZipFile('archive3.7z')
	try:
		zip_archive.extractall(pwd=i)
	except:
		pass

print(time.time() - starttime)	
file.close()
