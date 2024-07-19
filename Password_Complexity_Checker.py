import string

password=input("Enter the password to be checked: ")


uppercase=any([1 if p in string.ascii_uppercase else 0 for p in password])
lowercase = any([1 if p in string.ascii_lowercase else 0 for p in password])
special_char = any([1 if p in string.punctuation else 0 for p in password])
digits = any([1 if p in string.digits else 0 for p in password])

characters=[uppercase,lowercase,special_char,digits]

length=len(password)

score=0

with open('10-million-password-list-top-10000.txt', 'r') as f:
    common_pasword=f.read().splitlines()
    f.close()


if password in common_pasword:
    print("The entered password you entered was found in Common list, Change password!!")
    exit()

if length>=8:
    score+=1

print(f'Password length is {str(length)}.')

if sum(characters)>1:
    score+=1
if sum(characters)>2:
    score+=1
if sum(characters)>3:
    score+=1

print(f"Password has {sum(characters)} different character types.")

if score<2:
    print("The password is very weak:( You need to change the Password")
elif score==2:
    print("The password should be improved:|")
elif score==3:
    print("Nice..The password can be used:)")
else:
    print("Amazing!! The password is complex no one can find it out:>")
