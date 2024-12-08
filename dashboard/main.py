import streamlit as st


def calculate_percentage(number):
    if number <= 10:
        return 9
    elif number <= 20:
        return 22
    elif number <= 30:
        return 28
    elif number <= 40:
        return 36
    else:
        return 44


def main():
    st.title("Percentage Calculator")

    number = st.number_input(
        "Insert a number", value=None, placeholder="Type a number..."
    )

    col1, col2 = st.columns(2)

    if number:
        percentage = calculate_percentage(number)
        col1.metric("Tier", f"{percentage}%")
        col2.metric("Percent", (percentage*number)/100)


if __name__ == "__main__":
    main()

