import streamlit as st


def find_segments(number):
    if number <= 10000:
        return {
            number: (9 * number)/100
        }
    elif number <= 20000:
        return {
            "0-10000€": 900,
            f"10001-{number}€": (22 * (number-10000)) / 100
        }
    elif number <= 30000:
        return {
            "0-10000€": 900,
            "10001-20000€": 2200,
            f"20001-{number}€": (28 * (number-20000)) / 100
        }
    elif number <= 40000:
        return {
            "0-10000€": 900,
            "10001-20000€": 2200,
            "20001-30000€": 2800,
            f"30001-{number}€": (36 * (number-30000)) / 100
        }
    else:
        return {
            "0-10000€": 900,
            "10001-20000€": 2200,
            "20001-30000€": 2800,
            "30001-40000€": 3600,
            f"40001-{number}€": (44 * (number-40000)) / 100
        }


def main():
    st.title("Tax Calculator")

    number = st.number_input(
        "Insert a number", value=None, placeholder="Type a number..."
    )

    col1, col2 = st.columns(2)

    if number:
        segments = find_segments(number)
        col1.write("Calculated tax")
        col1.metric("Amount", f"{sum(segments.values())}€")
        col2.write("Tax breakdown")
        col2.write(segments)


if __name__ == "__main__":
    main()

