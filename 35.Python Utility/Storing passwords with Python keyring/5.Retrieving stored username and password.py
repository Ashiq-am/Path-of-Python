import keyring as kr

kr.set_password("GeeksforGeeks","Dwaipayan","Geeks@123")

cred = kr.get_credential("GeeksforGeeks","")

print("Username : ",cred.username)
print("Password : ",cred.password)
