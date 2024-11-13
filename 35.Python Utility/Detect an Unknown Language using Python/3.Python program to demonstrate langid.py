# Python program to demonstrate
# langid


import langid

L = ["Geeksforgeeks is a computer science portal for geeks",
     "Geeksforgeeks - это компьютерный портал для гиков",
     "Geeksforgeeks es un portal informático para geeks",
     "Geeksforgeeks是面向极客的计算机科学门户",
     "Geeksforgeeks geeks के लिए एक कंप्यूटर विज्ञान पोर्टल है",
     "Geeksforgeeksは、ギーク向けのコンピューターサイエンスポータルです。",
     ]

for i in L:
    # Language detection
    print(langid.classify(i))
