from pypdf import PdfReader
from langchain_core.documents import Document


def load_pdf(file_path):

    # Read PDF
    reader = PdfReader(file_path)

    documents = []

    # Extract text from each page
    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text and text.strip():

            document = Document(
                page_content=text,
                metadata={
                    "source": file_path,
                    "page": page_number + 1
                }
            )

            documents.append(document)

    return documents