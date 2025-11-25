import os
import random
import string
from typing import List, Optional

import streamlit as st


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images", "iStock-828766970.jpg")


def generate_random_password(
    length: int, include_numbers: bool = False, include_symbols: bool = False
) -> str:
    characters: str = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


def generate_memorable_password(
    no_of_words: int,
    separator: str,
    capitalization: bool = False,
    vocabulary: List[str] = [
        "organ",
        "hair",
        "pest",
        "define",
        "tendency",
        "test",
        "merit",
        "dairy",
        "slant",
        "country",
        "freshman",
        "offspring",
        "choose",
        "mill",
        "forbid",
    ],
) -> str:

    password_words = random.choices(vocabulary, k=no_of_words)

    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    password = separator.join(password_words)

    return password


def generate_pin(length: int) -> str:
    password = "".join(random.choice(string.digits) for _ in range(length))
    return password


st.title("Password Generator")

st.image(IMAGE_PATH, width=500)

selection = st.radio(
    "Choose your password type",
    ["Random Password", "Memorable Password", "PIN"],
)

if selection == "Random Password":
    length = st.slider(
        "Choose the length of your password:", min_value=4, max_value=100
    )
    include_numbers = st.toggle("Include numbers")
    include_symbols = st.toggle("Include symbols")

    finalize = st.button("Generate Password", type="primary")

    if finalize:
        generated = generate_random_password(length, include_numbers, include_symbols)
        st.success(rf"Your generated password: ``` {generated} ``` ")


if selection == "Memorable Password":
    no_of_words = st.slider(
        "Choose the number of your words:", min_value=3, max_value=15
    )
    separator = st.text_input("Separator:", value="_")
    capitalization = st.toggle("Capitalization")

    finalize = st.button("Generate Password", type="primary")

    if finalize:
        generated = generate_memorable_password(no_of_words, separator, capitalization)
        st.success(rf"Your generated password: ``` {generated} ``` ")


if selection == "PIN":
    length = st.slider("Length of password:", min_value=4)

    finalize = st.button("Generate Password", type="primary")

    if finalize:
        generated = generate_pin(length)
        st.success(rf"Your generated password: ``` {generated} ``` ")
