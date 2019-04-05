#!/usr/bin/python3

#import libraries
from zipfile import ZipFile
from tarfile import TarFile
from rarfile import RarFile

import time

NumberPasswords = 100

filename = 'passwords/passwords'+str(NumberPasswords)+'.txt'	#define password list file

file = open(filename,'r')	#open file for reading


passwords = [line.rstrip('\n') for line in file] # read line by line and strip newline characters

starttime = time.time()

for i in passwords:

	#zip_archive = ZipFile('archive1.zip')

	#try:

		#zip_archive.extractall(pwd=i)

	#except:

		#pass

	tar_archive = TarFile.open('archive5.tar')

	try:

		tar_archive.extractall(pwd=i)

	except:

		pass


	#rar_archive = patoolib.extract_archive('archive4.rar')
	rar_archive = RarFile("archive4.rar")
	try:

		rar_archive.extractall(pwd=i)

	except:

		pass

print(time.time() - starttime)
file.close()
