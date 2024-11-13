import random

def output(compliments):
	print(random.choice(tuple(compliments)))

def giveMe(isHe):
	she = [
		"I miss your grin.",
		"You're an incredible buddy.",
		"I can't believe I met someone like you.",
		"I feel thrilled every time I see you.",
		"I adore making you laugh.",
		"You're my greatest friend.",
		"I'll always have your back.",
		"I adore every inch of you— even your toes.",
		"You have a seductive personality.",
		"You're my queen.",
		"I miss you even when you haven't left yet.",
		"I feel happy to be with you.",
		"You always know how to make me feel at home.",
		"I can totally be myself with you," "I love your style.",
		"I love your style.",
	]
	he = [
		"What did you do to become in such great shape?\
		I'm interested in learning more about your training\
		regimen",
		"I like men who take care of themselves",
		"Wow, you're extremely gorgeous!",
		"What sort of deodorant are you wearing today? It smells\
		fantastic! ",
		"Your eyes have a nice look to them. I find it simple to\
		become lost in them. It really makes you look like you have\
		something deep to think about.",
		"Have you experimented with your hair? It appeals to me much.",
		"What sort of shoes are you wearing today? You should wear\
		it like that more often!",
		"Your posture is quite straight, which I admire. That must \
		have taken a long time for you to perfect ",
		"I'm quite impressed with how well you look after your health\
		. What do you do to keep your work-life balance?",
		"I admire how gentlemanly you are at all times. You are living\
		proof that chivalry still exists ",
		"You're very amusing. Your wonderful sense of humour is always\
		appreciated ",
		"I appreciate your thoughtfulness. Finding a man who is kind\
		might be challenging ",
		"I believe you comprehend what I'm saying. In the past, I've\
		had difficulty finding folks who comprehend what I'm saying \
		and thinking. I appreciate you always taking the time to learn\
		about me.",
		"I'm blown away by how composed you are in stressful situations\
		. It makes working through difficult situations a lot simpler. ",
		"You're incredibly good at active listening. I can always tell \
		whether you're paying attention to what I'm saying. That is \
		very appreciated ",
	]
	if isHe:
		output(he)
	else:
		output(she)
