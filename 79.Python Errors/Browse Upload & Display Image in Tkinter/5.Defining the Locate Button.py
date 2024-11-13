# adding background color to our upload button
app.option_add("*Label*Background", "white")
app.option_add("*Button*Background", "lightgreen")

label = tk.Label(app)
label.pack(pady=10)

# defining our upload buttom
uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
uploadButton.pack(side=tk.BOTTOM, pady=20)

app.mainloop()
