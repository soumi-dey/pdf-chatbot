import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 PDF Chatbot")
st.write("Upload your PDF and ask questions from it!")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    st.success(f"PDF loaded successfully! Total {len(reader.pages)} pages found.")
    
    question = st.text_input("Ask your question here:")

    if question:
        # Simple search - find matching lines from PDF
        words = question.lower().split()
        lines = text.split("\n")
        answer_lines = []
        for line in lines:
            if any(word in line.lower() for word in words if len(word) > 3):
                answer_lines.append(line)

        if answer_lines:
            st.write("### Answer found:")
            for line in answer_lines[:5]:
                st.write("- " + line)
        else:
            st.write("Sorry, no relevant information found in this PDF. Please try asking differently.")
