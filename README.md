Sure! Here's the complete English version of your `README.md`:

````markdown
# Chatbot Nobat Dehi

This project is a medical appointment chatbot built with Python and Streamlit.

## Project Description

The chatbot can respond to user queries related to:
- Booking an appointment  
- Rescheduling  
- Cancelling  
- Clinic address  
- Doctor's availability times

It uses machine learning models trained on intent data and responds based on user input.

## How to Run

1. First, install the required packages:

```bash
pip install -r requirements.txt
````

2. Then, run the chatbot using Streamlit:

```bash
streamlit run doctor.py
```

## Project Files

* `doctor.py`: Main chatbot script with Streamlit interface
* `output.json`: Intent data including possible questions and responses
* `tfidf_vectorizer_pkl`: Trained TF-IDF vectorizer
* `chatbot_model.pkl`: Trained machine learning model
* `.ipynb` notebooks: For training and testing the model
* `.gitignore`: (optional) to ignore unnecessary files

> Make sure all necessary files are located in the same folder as `doctor.py`, or update the file paths accordingly.

## Demo

After running the script, a chat interface will appear where users can interact with the assistant.
You can ask questions about appointments and receive smart replies.      
  
Let me know which version you prefer.
