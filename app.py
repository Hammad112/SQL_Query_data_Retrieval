import os
import sqlite3
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('google_api_key'))

# Function to load Gen AI Model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Defining Prompt
prompt = ["""
You are an expert in converting English questions to SQL queries!
The SQL database has the name STUDENT and has the following columns:
- Student_id
- First_Name
- Last_Name
- Degree_Name
- Section_Name
- Age
- Marks

\n\nFor example,
Example 1 - How many entries of records are present?, 
the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

\nExample 2 - Tell me all the students studying in Computer Systems Engineering?, 
the SQL command will be something like this: SELECT * FROM STUDENT WHERE Degree_Name="Computer Systems Engineering";

Also, the SQL code should not have ``` in the beginning or end, and there should be no mention of the word SQL in the output.
"""

]

## Streamlit App

st.set_page_config(page_title="SQL query Generator")
st.header("SQL Data and Query Retrieval")

# Add custom CSS for input styling
st.markdown("""
    <style>
        .css-1n7v3ny edgvbvh3 {
            border: 2px solid green;
        }
    </style>
""", unsafe_allow_html=True)

# Input field
question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print("Generated SQL Query:", response)  # Debugging output for the generated SQL query
    
    # Display the generated SQL query in a code block
    st.subheader("Generated SQL Query:")
    st.code(response, language='sql')

    # Execute the SQL query and retrieve results
    response = read_sql_query(response, "student.db")
    
    # Display the response from the SQL query
    st.subheader("The Response is")
    for row in response:
        st.text(row)
