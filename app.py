import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key='AIzaSyBMFWrHTjUzBxzDdrOiWh77T0zrnkdp51M')

# Function to load Gen AI Model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Defining Prompt
prompt = ["""
You are an expert in converting English questions to SQL queries!
The SQL database has various tables and columns, and your job is to generate SQL queries based on user questions.

\nFor example,
Example 1 - How many records are present?, 
the SQL command will be something like this: SELECT COUNT(*) FROM [table_name];

\nExample 2 - List all students with a specific degree?, 
the SQL command will be something like this: SELECT * FROM [table_name] WHERE [degree_column]="[specific_degree]";

Ensure that the generated SQL code does not include ``` at the beginning or end, and do not mention the word SQL in the output.
"""

]

## Streamlit App

st.set_page_config(page_title="Generic SQL Query Generator")
st.header("Generic SQL Query Generator")

# Add custom CSS for input styling
st.markdown("""
    <style>
        .css-1n7v3ny edgvbvh3 {
            border: 2px solid green;
        }
    </style>
""", unsafe_allow_html=True)

# Input field
question = st.text_input("Input your question about the database:", key="input")

submit = st.button("Generate SQL Query")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print("Generated SQL Query:", response)  # Debugging output for the generated SQL query
    
    # Display the generated SQL query in a code block
    st.subheader("Generated SQL Query:")
    st.code(response, language='sql')

    # Provide feedback to the user
    st.write("This is the generated SQL query based on your question.")
