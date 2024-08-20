import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.title("PDF Viewer")

# with st.sidebar:
#     pdf_viewer("test_pdf.pdf", key = "step-01")

tab1, tab2 = st.tabs(["Step 01", "Step 02"])

with tab1:
    st.title("Image Classification")

with tab2:
    pdf_viewer("test_pdf.pdf", key = "step-02")