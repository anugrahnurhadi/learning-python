#By Anugrah Noer Hadi
#This code is an example to validate username and password with certain rules.
#Rules for Username:
#1.Username contains morethan 5 and 9 characters that are alphabet, numbers, and symbols, and space is not allowed.
#2.Username has to begin with alphabet.
#Rules for Password:
#1.Password must be more than 8 chaeacters including at least 1 uppercase, 1 lowercase, 1 numbers, and 1 special symbuls and must contains '@'
#
#If the rules for username is fulfilled, the program will return true values.
#If the rules for username is fulfilled, the program will return true values.

def is_username(username):
	alnum=0
	char=0
	if (len(username)>=5) and (len(username)<=9) and (username[0].isalpha()==1) and (username.count(' ')==0):
		return bool(1)
	else:
		return bool(0)
		
			
def is_passwd(passwd):
	num=0
	upper=0
	lower=0
	char=0
	if (len(passwd)>=8) and (passwd.count('@')>0):
		for pas in passwd:
			if (pas.isnumeric()==1):
				num=num+1
			if (pas.isupper()==1):
				upper=upper+1
			if (pas.islower()==1):
				lower=lower+1
			if (pas.isalnum()==0) and (pas.isspace()==0):
				char=char+1
		
		if (char>0) and (upper>0) and (lower>0) and (num>0):
			return bool(1)
		else:
			return bool(0)
	else:
		return bool(0)

username=input("Masukan Username : ")
print(is_username(username))
passwd=input("Masukan Password : ")	
print(is_passwd(passwd))

def countphrase(allstring,selected):
    if len(allstring)>len(selected):
        allstring.r