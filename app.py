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

def main():
    st.title("Python Compiler")

    # Get Python code from user input
    code = st.text_area("Enter Python code:", height=200)

    # Display output
    if st.button("Run Code"):
        # Capture the output of the code
        output = capture_stdout(lambda: exec(code))
        
        # Display the captured output
        st.markdown("### Output:")
        st.code(output)

if __name__ == "__main__":
    main()
