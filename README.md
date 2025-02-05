# Streamlit Summarizer App

This is a simple Streamlit web application that allows users to input text and receive a summarized version of their text. The application is designed to provide an easy-to-use interface for text summarization.

## Project Structure

```
summarizer-app
├── src
│   ├── app.py          # Main entry point of the Streamlit application
│   └── summarizer.py   # Contains the logic for summarizing text
├── requirements.txt    # Lists the dependencies required for the project
└── README.md           # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd summarizer-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   Make sure your python version is greater than 3.8.

## Usage

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run src/app.py
```

Once the application is running, you can enter your text in the provided textbox, and the summarized version will be displayed below.
