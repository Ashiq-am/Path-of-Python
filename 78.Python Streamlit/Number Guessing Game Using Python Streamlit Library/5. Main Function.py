def main():
    st.write(
        """
        # Guess The Number !!
        """
    )
    if 'number' not in st.session_state:
        initial_state()

    st.button('New game', on_click=restart_game)
    placeholder, debug, hint_text = st.empty(), st.empty(), st.empty()
    guess = placeholder.number_input(
        f'Enter your guess from 1 - {100}',
        key=st.session_state.input,
        min_value=0,
        max_value=100,
    )

    col1, _, _, _, col2 = st.columns(5)
    with col1:
        hint = st.button('Hint')

    with col2:
        if not guess:
            st.write(f"Attempt Left : 7")
        if guess:
            st.write(f"Attempt Left : {6-st.session_state.attempt}")

    if hint:
        hint_response = get_hint(st.session_state.number)
        hint_text.info(f'{hint_response}')

    if guess:
        if st.session_state.attempt < 6:
            st.session_state.attempt += 1
            if guess < st.session_state.number:
                debug.warning(f'{guess} is too low!')
            elif guess > st.session_state.number:
                debug.warning(f'{guess} is too high!')
            else:
                debug.success(
                    f'Yay! you guessed it right '

                )
                st.balloons()
                st.session_state.over = True
                placeholder.empty()
        else:
            debug.error(
                f'Sorry you Lost! The number was {st.session_state.number}'
            )

            st.session_state.over = True
            placeholder.empty()
            hint_text.empty()


if __name__ == '__main__':
    main()
