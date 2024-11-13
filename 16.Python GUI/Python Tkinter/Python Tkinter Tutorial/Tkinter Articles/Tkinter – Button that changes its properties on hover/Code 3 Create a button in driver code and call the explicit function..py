# Driver Code 
root = Tk() 

# create button 
# assign button text along 
# with background color 
myButton = Button(root, 
				text="On Hover - Background Change", 
				bg="yellow") 
myButton.pack() 

# call function with background 
# colors as argument 
changeOnHover(myButton, "red", "yellow") 

root.mainloop() 
