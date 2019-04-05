#import libraries
import random
import string

PasswordLength = 12
NumberPasswords = 100

filename = 'passwords/passwords'+str(NumberPasswords)+'.txt'	#define password list file
file = open(filename,'w')	#open file for writing


#define function that create random ASCII strings/numbers
def randomString(stringLength = PasswordLength):
    letters = string.ascii_letters
	numbers = string.digits
    return ''.join(random.choice(letters + numbers) for i in range(stringLength))

for i in range(1,NumberPasswords):
	file.write(randomString()+'\n')		#call randomString and write it to file 100x
	i += 1

file.close()
print(filename,'created.') 