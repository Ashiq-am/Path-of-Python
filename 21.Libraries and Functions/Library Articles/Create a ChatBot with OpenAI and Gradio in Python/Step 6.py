block = gradio.Blocks(theme=gradio.themes.Monochrome())
with block:
	gradio.Markdown("""<h1><center>ChatGPT ChatBot 
	with Gradio and OpenAI</center></h1> 
	""")
	chatbot = gradio.Chatbot()
	message = gradio.Textbox(placeholder=prompt)
	state = gradio.State()
	submit = gradio.Button("SEND")
	submit.click(message_and_history,
				inputs=[message, state],
				outputs=[chatbot, state])
block.launch(debug = True)
