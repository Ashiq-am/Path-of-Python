def Translate():
	try:
		translator = Translator(to_lang=dest_lang.get())
		translation = translator.translate(Input_text.get())
		Output_text.delete(1.0, END)
		Output_text.insert(END, translation)
	except Exception as e:
		print(f"Translation error: {e}")
