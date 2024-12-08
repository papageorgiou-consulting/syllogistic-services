import streamlit as st


def calculate_percentage(number):
    if number <= 10000:
        return (9 * number)/100
    elif number <= 20000:
        return 900 + (22 * (number-10000)) / 100
    elif number <= 30000:
        return 900 + 2200 + (28 * (number-20000)) / 100
    elif number <= 40000:
        return 900 + 2200 + 2800 + (36 * (number-30000)) / 100
    else:
        return 900 + 2200 + 2800 + 3600 + (44 * (number-40000)) / 100


def main():
    st.title("Percentage Calculator")

    number = st.number_input(
        "Insert a number", value=None, placeholder="Type a number..."
    )

    col1, col2 = st.columns(2)

    if number:
        percentage = calculate_percentage(number)
        col1.metric("Tax", f"{percentage}€")


if __name__ == "__main__":
    main()

