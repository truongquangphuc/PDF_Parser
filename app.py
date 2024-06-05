import os
import nest_asyncio
from llama_parse import LlamaParse  # pip install llama-parse
from llama_index.core import SimpleDirectoryReader  # pip install llama-index
from dotenv import load_dotenv
import streamlit as st

nest_asyncio.apply()
# Load environment variables
load_dotenv()

def extract_text_from_pdf(pdf_path):
    documents = LlamaParse(language="vi", result_type="markdown").load_data(pdf_path)
    return documents[0].text if documents else ""

st.title("PDF_Parser")
uploaded_file = st.file_uploader("Chọn file PDF của bạn", type="pdf")
if uploaded_file is not None:
    # Lưu tệp tải lên vào một tệp tạm thời
    temp_file_path = os.path.join("/tmp", uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Trích xuất văn bản từ tệp PDF tạm thời
    text_data = extract_text_from_pdf(temp_file_path)

    st.header("Extracted Text")
    st.text_area("Extracted Text", value=text_data, height=400)
    
    st.download_button(
        label="Download Extracted Text",
        data=text_data,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

    # Xóa tệp tạm thời sau khi sử dụng
    os.remove(temp_file_path)
