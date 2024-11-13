st.title("ChatGPT ChatBot With Streamlit and OpenAI")
if 'user_input' not in st.session_state:
	st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
	st.session_state['openai_response'] = []

def get_text():
	input_text = st.text_input("write here", key="input")
	return input_text

user_input = get_text()

if user_input:
	output = api_calling(user_input)
	output = output.lstrip("\n")

	# Store the output
	st.session_state.openai_response.append(user_input)
	st.session_state.user_input.append(output)
