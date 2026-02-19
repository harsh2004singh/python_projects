import streamlit as st
import random
import time

# ---------- Functions ----------
def mistake(paragraphtest, usertest):
    error = 0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_calculator(time_start, time_end, userinput):
    time_delay = time_end - time_start
    speed = len(userinput) / time_delay
    return round(speed, 2)

# ---------- UI ----------
st.title("⌨️ Typing Speed Calculator")

test_strings = [
    "apple",
    "banana",
    "mango",
    "grapes",
    "orange",
    "pineapple",
    "kiwi"
]

# session state to keep same word during typing
if "random_string" not in st.session_state:
    st.session_state.random_string = random.choice(test_strings)

st.subheader("Type this word 👇")
st.code(st.session_state.random_string)

# start timer when user starts typing
if "start_time" not in st.session_state:
    st.session_state.start_time = None

user_input = st.text_input("Start typing here:")

if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# button to submit
if st.button("Submit"):
    if st.session_state.start_time is not None:
        end_time = time.time()

        speed = speed_calculator(
            st.session_state.start_time, end_time, user_input
        )
        errors = mistake(st.session_state.random_string, user_input)

        st.success(f"Speed: {speed} characters/sec")
        st.error(f"Errors: {errors}")

        # new word for next round
        st.session_state.random_string = random.choice(test_strings)
        st.session_state.start_time = None
