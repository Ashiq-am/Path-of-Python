import streamlit as st
import random


def get_secret_number():
    return random.randint(1, 100)
