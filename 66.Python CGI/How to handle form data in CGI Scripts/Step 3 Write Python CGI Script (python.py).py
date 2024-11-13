#!C:\Program Files\Python311\python.exe

print("Content-type: text/html\n\n")
import cgi

# Get form data
form = cgi.FieldStorage()

# Retrieve values from the form
name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')

# HTML response
print("<html>")
print("<head>")
print("<title>Registration Confirmation</title>")
print("<style>")
print(" /* Style for the card container */")
print(" .card {")
print(" width: 300px;")
print(" padding: 20px;")
print(" margin: 20px auto;")
print(" border: 1px solid #ccc;")
print(" border-radius: 5px;")
print(" text-align: center;")
print(" }")
print("</style>")
print("</head>")
print("<body>")
print("<div class='card'>")
print("<h2>Registration Confirmation</h2>")
print("<p>Name: " + name + "</p>")
print("<p>Email: " + email + "</p>")
# You should never display passwords like this in a real application; this is just for demonstration purposes
print("<p>Password: " + password + "</p>")
print("<p>Registration Successful! </p>") # Emoji for success
print("</div>")
print("</body>")
print("</html>")
