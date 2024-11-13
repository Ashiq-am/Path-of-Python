import streamlit as st
from gramformer import Gramformer
from autocorrect import Speller
import subprocess

st.title("Grammar Corrector")

user_input = st.text_area("Enter Text Here")

def process(text):
    command = "python -m spacy download en"
    subprocess.run(command, shell=True)
    gf = Gramformer(models=1, use_gpu=False)
    spell = Speller()
    corrected = spell(text)
    ans = ""
    res = gf.correct(corrected)
    for ele in res:
        ans += ele
    return ans


if st.button("Process"):
    processed_text = process(user_input)
    st.subheader("Corrected Text:")
    st.write(processed_text)
