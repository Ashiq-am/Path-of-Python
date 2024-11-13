# now get auther infromation
# with auther name
profile ='https://auth.geeksforgeeks.org/user/'+Author+'/profile'

# pass the url
# into getdata function
htmldata=getdata(profile)
soup = BeautifulSoup(htmldata, 'html.parser')
