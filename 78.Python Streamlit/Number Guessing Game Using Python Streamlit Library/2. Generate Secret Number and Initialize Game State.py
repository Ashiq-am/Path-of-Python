def initial_state(post_init=False):
    if not post_init:
        st.session_state.input = 0
    st.session_state.number = get_secret_number()
    st.session_state.attempt = 0
    st.session_state.over = False
