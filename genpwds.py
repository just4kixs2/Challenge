#import libraries
import random
import string

PasswordLength = 12
NumberPasswords = 100

filename = 'passwords/passwords'+str(NumberPasswords)+'.txt'	#define password list file
file = open(filename,'w')	#open file for writing


#define function that create random ASCII letters/digits
def randomString(stringLength = PasswordLength):
    letters = string.ascii_letters
    digits = string.digits
    return ''.join(random.choice(letters + digits) for i in range(stringLength))

for i in range(1,NumberPasswords):
	file.write(randomString()+'\n')		#call randomString and write it to passwords file
	i += 1

file.close()
print(filename,'created.') 
