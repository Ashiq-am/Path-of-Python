import keyring as kr

kr.set_password("GeeksforGeeks",
				"Dwaipayan",
				"Geeks@123")

print("Before deleting password ",
	kr.get_password("GeeksforGeeks",
					"Dwaipayan"))

kr.delete_password("GeeksforGeeks", "Dwaipayan")

print("After deleting Password",
	kr.get_password("GeeksforGeeks", "Dwaipayan"))
