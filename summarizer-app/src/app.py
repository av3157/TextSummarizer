import streamlit as st
from summarizer import summarize_text

def main():
    st.title("Text Summarizer")
    st.write("Enter the text you want to summarize below:")

    user_input = st.text_area("Input Text", height=300)
    num_sents = st.slider("Max Number of Sentences in Summary", min_value=1, max_value=10)

    if st.button("Summarize"):
        if user_input and num_sents:
            summary = summarize_text(user_input, num_sents)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize and a desired length for the summary.")

if __name__ == "__main__":
    main()