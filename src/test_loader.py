from src.loader import load_pdf

pdf_path = "data/pdfs/sample.pdf"

documents = load_pdf(pdf_path)

print("Total pages loaded:", len(documents))

for document in documents:

    print("\n--------------------")

    print("Page:", document.metadata["page"])

    print("Source:", document.metadata["source"])

    print("Extracted text:")

    print(document.page_content[:500])