# app.py
import streamlit as st
from io import StringIO
import sys

def capture_stdout(func):
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    try:
        func()
        return new_stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def execute_code(user_code):
    try:
        # Replace `input()` calls with a predefined value (e.g., "10")
        user_code = user_code.replace("input(", '"10" # input(')
        exec(user_code, {})
    except Exception as e:
        return str(e)

    return capture_stdout(lambda: exec(user_code, {}))

def main():
    st.title("Python Compiler")

    # Get Python code from user input
    code = st.text_area("Enter Python code:", height=200)

    # Display output
    if st.button("Run Code"):
        output = execute_code(code)
        
        # Display the captured output
        st.markdown("### Output:")
        st.code(output)

if __name__ == "__main__":
    main()
