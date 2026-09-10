import getpass

username = 'ivory'
password = 'cavory12'

p = ( 'input username ---> ')

u = getpass.getpass ( 'input password ---> ')

if username == p and u == password :
     		print("access granted")

else :
	print("access denied")