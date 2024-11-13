message_history = st.empty()

if st.session_state['user_input']:
	for i in range(len(st.session_state['user_input']) - 1, -1, -1):
		# This function displays user input
		message(st.session_state["user_input"][i],
				key=str(i), avatar_style="icons")
		# This function displays OpenAI response
		message(st.session_state['openai_response'][i],
				avatar_style="miniavs", is_user=True
				, key=str(i) + 'data_by_user')
