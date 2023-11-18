import streamlit as st

def main():
    st.title("Python Compiler")

    # Get Python code from user input
    code = st.text_area("Enter Python code:", height=200)

    # Display output
    if st.button("Run Code"):
        # You would normally send the code to a backend, but for simplicity, we'll just display it here
        st.markdown("### Output:")
        exec_output = eval(code)
        st.code(str(exec_output))

if __name__ == "__main__":
    main()
