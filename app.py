import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import requests

# Title of the app
st.title("GitHub PDF Viewer")

# URL of the PDF file in the GitHub repository
# sample url -> "https://raw.githubusercontent.com/yourusername/yourrepository/branch/yourfile.pdf"
pdf_url = "https://raw.githubusercontent.com/LachinFernando/pdf_viewer/main/test_pdf.pdf"

# Fetch the PDF file from GitHub
response = requests.get(pdf_url)

# Check if the request was successful
if response.status_code == 200:
    # Display the PDF in the Streamlit app
    st.download_button(label="Download PDF", data=response.content, file_name="downloaded.pdf")
    if st.button("Show PDF"):
        with st.sidebar:
            pdf_viewer(response.content)
    
else:
    st.error("Failed to fetch PDF file. Please check the URL.")