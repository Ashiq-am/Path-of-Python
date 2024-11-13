chatbot = ChatBot(
	'JARVIS',
	logic_adapters=[
		'chatterbot.logic.BestMatch',
		'chatterbot.logic.TimeLogicAdapter'],
)
