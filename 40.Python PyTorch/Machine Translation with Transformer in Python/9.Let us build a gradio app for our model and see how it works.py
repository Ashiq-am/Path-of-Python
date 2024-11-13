import gradio as gr


def translate(text):
    inputs = tokenizer(text, return_tensors="pt").to(device)
    translated_tokens = model.generate(**inputs, max_length=256)
    results = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

    return results


#Creating the User Interface Space
interface = gr.Interface(fn=translate,inputs=gr.Textbox(lines=2, placeholder='Text to translate'),
						outputs='text')
#launching the interface
interface.launch()
