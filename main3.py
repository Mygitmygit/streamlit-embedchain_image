__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import streamlit as st
#아래 두줄은 로컬환경에서 실행할때만 활성화해준다.
#from dotenv import load_dotenv
#load_dotenv()


# 사용자정의함수 정의----------------------------------------
import os
import PyPDF2
from embedchain import App



pdf_bot = App()

pdf_text=""

with open("data.pdf","rb") as pdf_file:
   pdf_reader = PyPDF2.PdfReader(pdf_file)
   num_pages = len(pdf_reader.pages)


   for page_num in range(num_pages):
     page = pdf_reader.pages[page_num]
     page_text = page.extract_text()
     pdf_text += page_text

pdf_bot.add(pdf_text,data_type="text")
#----------------------------------------------------------



# Function to process input and return output
def process_input(input_text):
    processed_output = pdf_bot.chat(input_text)
    return processed_output

# Streamlit app
def main():
    image = st.image("image.JPG")

    # Input box for user input
    user_input = st.text_input("질문을 입력해주세요:")

    # Process input when the user submits
    if st.button("질문하기"):
        processed_output = process_input(user_input)
        # Display the processed output
        st.text("답변:")
        st.write(processed_output)

if __name__ == "__main__":
    main()